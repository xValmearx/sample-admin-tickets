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


class ProjectDetailView(DetailView):
    """Show open tickets for project"""

    model = Project
    template_name = "project_detail.html"


class ProjectDetailClosedView(DetailView):
    """show clsoed tickets for project"""

    model = Project
    template_name = "project_detail_closed.html"


class ProjectCreateView(CreateView):
    """Create a new project"""

    model = Project
    template_name = "project_create.html"
    fields = ["name", "members"]

    def get_success_url(self):
        messages.success(self.request, "Project Created Successfully")
        return reverse("project_list")


class ProjectEditView(UpdateView):
    """UPdate the details for a project"""

    model = Project
    template_name = "project_update.html"
    fields = ["name", "members"]

    def get_success_url(self):
        messages.success(self.request, "Project Updated Successfully")
        return reverse("project_list")


class TicketCreateView(CreateView):
    """Create a new ticket"""


class TicketEditView(UpdateView):
    """Update an existing ticket"""
