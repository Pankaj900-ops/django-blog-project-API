from django.urls import path, include
from rest_framework import routers
from .views import BlogPostViewSet, blog_list, blog_detail, api_blog_list, api_blog_detail, api_load_more, api_blog_like

# DRF router for API
router = routers.DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='posts')

urlpatterns = [
    # Frontend pages
    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),

    # Extra APIs
    path('api/blog-list/', api_blog_list, name='api_blog_list'),
    path('api/blog-detail/<int:post_id>/', api_blog_detail, name='api_blog_detail'),
    path('api/load-more/', api_load_more, name='api_load_more'),
    path('blog/<int:post_id>/like/', api_blog_like, name='like_post'),

    # DRF ViewSet router
    path('api/', include(router.urls)),
]

