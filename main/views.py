from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo as Author
from .models import Project, Skill, Education, Work

# Create your views here.

def index(request):

    author = Author.objects.get(pk=1)
    projects = Project.objects.all()

    skills = Skill.objects.all()
    edu = Education.objects.all()
    work = Work.objects.all()


    return render(
        request, 
        'index.html', 
        {
            'author': author, 
            'projects': projects, 
            'skills': skills, 
            'edus': edu,
            'works': work
        }
    )
