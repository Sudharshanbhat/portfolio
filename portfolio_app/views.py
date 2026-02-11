from django.shortcuts import render, redirect
from .models import Skill, Project, ContactMessage
from .forms import ContactForm


def portfolio_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = ContactForm()

    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'skills': skills,
        'projects': projects,
        'form': form,
    }
    return render(request, 'portfolio.html', context)
