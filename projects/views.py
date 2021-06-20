"""Projects views"""

# django
from django.shortcuts import render

# projects models
from projects.models import Project


def project_index(request):
    """Return all projects"""

    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    """Return detailed project"""

    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
