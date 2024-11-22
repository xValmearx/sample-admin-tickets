from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
)

from django.urls import reverse

from .models import Project, Ticket


class ProjectListView(ListView):
    """Show lit of projects"""

    model = Project
    template_name = "project_list.html"
