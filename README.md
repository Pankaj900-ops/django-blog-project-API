
# Django Blog Application (Ready-made)

This is a ready-made Django + DRF blog application scaffold with JWT auth, MySQL-ready settings, CKEditor placeholders,
and a simple responsive frontend using Django templates and AJAX "Load More".

## Features
- JWT authentication (djangorestframework-simplejwt) for API.
- BlogPost model with title, content (rich text), author, timestamp, status (draft/published).
- DRF API endpoints for CRUD with permission checks (only authors can edit/delete their posts).
- Pagination (10 posts per page) on the API.
- Django templates for listing and reading posts, with a "Load More" button that loads posts via AJAX.
- Admin customizations for BlogPost and User.
- Requirements file included.
- README with setup steps and placeholders for MySQL credentials (update before migrate).

## What you need to do
1. Install Python (3.10+ recommended) and create a virtualenv.
2. Install dependencies: `pip install -r requirements.txt`
3. Update `blog_project/settings.py` DATABASES section with your MySQL credentials.
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver`
7. Push to GitHub and deploy to your preferred cloud platform (e.g., Heroku, Railway, Render, etc.).

## Notes
- CKEditor is set up in INSTALLED_APPS and forms but requires `pip install django-ckeditor` and static setup.
- JWT endpoints use simplejwt; configure token lifetime in settings if needed.
- A `.env` mechanism is recommended for production database credentials and SECRET_KEY management.
