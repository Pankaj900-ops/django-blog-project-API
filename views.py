from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsAuthorOrReadOnly

# --------------------------
# DRF Pagination
# --------------------------
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10

# --------------------------
# DRF ViewSet
# --------------------------
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(status='published').select_related('author')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title','content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# --------------------------
# Frontend Views
# --------------------------
def blog_list(request):
    posts = BlogPost.objects.filter(status='published').order_by('-timestamp')[:10]
    return render(request, 'blog_app/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, status='published')
    return render(request, 'blog_app/blog_detail.html', {'post': post})

# --------------------------
# API Views
# --------------------------
@api_view(['GET'])
def api_blog_list(request):
    posts = BlogPost.objects.filter(status='published').order_by('-timestamp')
    data = [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'timestamp': post.timestamp.strftime('%Y-%m-%d %H:%M'),
            'total_likes': post.total_likes()
        }
        for post in posts
    ]
    return Response({'posts': data})

@api_view(['GET'])
def api_blog_detail(request, post_id):
    try:
        post = BlogPost.objects.get(id=post_id, status='published')
    except BlogPost.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'timestamp': post.timestamp.strftime('%Y-%m-%d %H:%M'),
        'total_likes': post.total_likes()
    }
    return Response(data)

def api_load_more(request):
    page = int(request.GET.get('page', '1'))
    posts_qs = BlogPost.objects.filter(status='published').order_by('-timestamp')
    paginator = Paginator(posts_qs, 10)
    try:
        page_obj = paginator.page(page)
    except:
        return JsonResponse({'results': []})

    data = [
        {
            'id': p.id,
            'title': p.title,
            'author': p.author.username,
            'timestamp': p.timestamp.strftime('%Y-%m-%d %H:%M'),
            'excerpt': p.content[:200],
            'total_likes': p.total_likes()
        }
        for p in page_obj.object_list
    ]
    return JsonResponse({'results': data, 'has_next': page_obj.has_next()})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_blog_like(request, post_id):
    try:
        post = BlogPost.objects.get(id=post_id, status='published')
    except BlogPost.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return Response({
        'liked': liked,
        'total_likes': post.total_likes()
    })
