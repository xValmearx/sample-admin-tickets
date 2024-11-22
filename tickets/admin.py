from django.contrib import admin
from adminlte2_pdq.admin_menu import AdminMenu

# Register your models here.
from .models import Project, Ticket

admin.site.register(Project)
AdminMenu.set_model_icon("Project", "fa fa-archive")

admin.site.register(Ticket)
AdminMenu.set_model_icon("Ticket", "fa fa-ticket")

AdminMenu.set_app_icon("Tickets", "fa fa-snowflake-o")


# set icons fo built-on user Auth here since we
# dont have an accounts app. Otherwise, it would make sense for them to be defined there

AdminMenu.set_model_icon("Group", "fa fa-users")
AdminMenu.set_model_icon("User", "fa fa-user")
AdminMenu.set_app_icon("Authentication and Authorization", "fa fa-user-o")
