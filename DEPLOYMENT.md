
# Deployment notes
- Use environment variables for SECRET_KEY and DATABASE credentials.
- On platforms like Railway/Render/Heroku, set up buildpacks and MySQL add-on or use external RDS.
- Collect static files when deploying: `python manage.py collectstatic`
- For production set DEBUG=False and configure ALLOWED_HOSTS.
