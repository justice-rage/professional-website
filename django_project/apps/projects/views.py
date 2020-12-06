from django.shortcuts import render
from projects.models import Project

# Create your views here.
def all_projects(request):
    # query database to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/projects_index.html',
                    {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/projects_detail.html',
                    {'project': project})

def project_technology(request, technology):
    projects = Project.objects.filter(
        technology__name__contains=technology
    )
    context = {
        "technology": technology,
        "projects": projects
    }
    return render(request, "projects/projects_technology.html", context)