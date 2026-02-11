import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'porfolio.settings')
django.setup()

from portfolio_app.models import Skill, Project

# Add sample skills
Skill.objects.all().delete()
skills_data = [
    {"title": "Frontend", "description": "HTML, CSS, Responsive Design"},
    {"title": "Backend", "description": "Python, Java, Django"},
    {"title": "Database", "description": "MongoDB, SQL, SQLite"},
    {"title": "Services", "description": "Web Apps, API Development, UI Design"},
]

for skill in skills_data:
    Skill.objects.create(**skill)
    print(f"Created skill: {skill['title']}")

# Add sample projects
Project.objects.all().delete()
projects_data = [
    {"title": "E-commerce Platform", "description": "Full-stack web application with Django and React"},
    {"title": "Chat Application", "description": "Real-time chat app built with Django and WebSockets"},
    {"title": "Task Management Tool", "description": "Productivity app with Django backend"},
]

for project in projects_data:
    Project.objects.create(**project)
    print(f"Created project: {project['title']}")

print("Sample data added successfully!")
