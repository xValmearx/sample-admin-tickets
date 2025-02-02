from django.db import models

# Choices for the Priority field on the Ticket Model

PRIORITY_CHOICES = (
    (1, "Expedite"),
    (2, "High"),
    (3, "Medium"),
    (4, "Low"),
    (5, "None"),
)


class Project(models.Model):
    """Represents a project"""

    name = models.CharField(max_length=200)
    members = models.ManyToManyField("auth.User")
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        """string conversion"""
        return f"{self.name}"

    def open_tickets(self):
        """Get all open tickets"""

        return self.tickets.filter(complete=False)

    def closed_tickets(self):
        """Get all closed tickets"""
        return self.tickets.filter(complete=True)

    def expedite_priority(self):
        """Get ticket with high priority"""
        return self.tickets.filter(priority=1, complete=False)

    def high_priority(self):
        """Get ticket with high priority"""
        return self.tickets.filter(priority=2, complete=False)

    def medium_priority(self):
        """Get ticket with high priority"""
        return self.tickets.filter(priority=3, complete=False)

    def low_priority(self):
        """Get ticket with high priority"""
        return self.tickets.filter(priority=4, complete=False)

    def no_priority(self):
        """Get ticket with high priority"""
        return self.tickets.filter(priority=5, complete=False)


class Ticket(models.Model):
    """Represent a ticket for a Porject"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tickets")

    assigned_to = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="tickets", blank=True, null=True
    )

    name = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    complete_by = models.DateField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String convertions"""

        return f"{self.project} - {self.name}"
