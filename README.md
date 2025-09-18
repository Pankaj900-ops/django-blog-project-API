# 📝 Django Blog Project

A simple **Blog Application** built with **Django & Django REST Framework (DRF)**.  
It supports blog post CRUD, like/unlike functionality, load more posts with pagination, and REST APIs.

---

## 🚀 Features
- User Authentication (login/register)
- Create, Read, Update, Delete blog posts
- Like & Unlike posts
- REST API with DRF (pagination, filtering, search)
- Responsive UI with static files (CSS)
- Admin panel for managing posts
- Share posts on Twitter & Facebook
- Load more posts dynamically

---

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: MySQL / SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
blog_project/ # Main Django project
blog_app/ # Blog application
static/ # CSS, JS, images
templates/ # HTML templates
manage.py # Django manager
requirements.txt # Python dependencies
README.md # Documentation
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog

Create & activate virtual environment
python -m venv myenv
myenv\Scripts\activate    # On Windows
source myenv/bin/activate # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Default: SQLite (works out of the box)

For MySQL: Update settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create superuser
python manage.py createsuperuser

7️⃣ Run server
python manage.py runserver

🔗 URLs

Home Page (Blog List) → http://127.0.0.1:8000/blog/

Blog Detail → http://127.0.0.1:8000/blog/<id>/

Like Post API (POST) → http://127.0.0.1:8000/blog/<id>/like/

API Blog List → http://127.0.0.1:8000/api/blog-list/

API Load More (GET) → http://127.0.0.1:8000/api/load-more/?page=2

Admin Panel → http://127.0.0.1:8000/admin/

📌 API Examples
1️⃣ Get Blog List
GET /api/blog-list/


Response

{
  "posts": [
    {
      "id": 1,
      "title": "My First Blog",
      "content": "This is a test blog.",
      "author": "admin",
      "timestamp": "2025-09-17 14:30",
      "total_likes": 3
    }
  ]
}

2️⃣ Like / Unlike Post
POST /blog/1/like/


Response

{
  "liked": true,
  "total_likes": 4
}

🎨 Static Files

Place CSS files in /static/

Example: static/style.css

Link in template:

<link rel="stylesheet" href="{% static 'style.css' %}">

✅ Requirements

Python 3.10+

Django 4+

Django REST Framework

MySQL (optional) / SQLite

🤝 Contribution

Fork this repo

Create a new branch (feature-xyz)

Commit changes

Push branch & create a Pull Request

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Pankaj Jadhav ✨

