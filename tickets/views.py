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

    model = Ticket
    template_name = "ticket_create.html"
    fields = ["name", "description", "priority", "complete_by", "complete"]

    def get(self, request, project_pk, *args, **kwargs):
        """Handel Get Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def post(self, request, project_pk, *args, **kwargs):
        """Handle Post Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def get_context_data(self):
        """add veribles to the template context"""
        context = super().get_context_data()
        context["project"] = Project.objects.get(pk=self.project_pk)
        return context

    def form_valid(self, form):
        """code to run when is valid"""
        form.instance.project = Project.objects.get(pk=self.project_pk)
        return super().form_valid(form)

    def get_success_url(self):
        """return the location to the redirect"""
        messages.success(self.request, "Ticket Created Successfully")
        return reverse("project_detail", kwargs={"pk": self.project_pk})


class TicketEditView(UpdateView):
    """Update an existing ticket"""

    model = Ticket
    template_name = "ticket_create.html"
    fields = ["name", "description", "priority", "complete_by", "complete"]

    def get(self, request, project_pk, *args, **kwargs):
        """Handel Get Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def post(self, request, project_pk, *args, **kwargs):
        """Handle Post Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def get_context_data(self):
        """add veribles to the template context"""
        context = super().get_context_data()
        context["project"] = Project.objects.get(pk=self.project_pk)
        return context

    def get_success_url(self):
        """return the location to the redirect"""
        messages.success(self.request, "Ticket Updated Successfully")
        return reverse("project_detail", kwargs={"pk": self.project_pk})
