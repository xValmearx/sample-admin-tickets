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

        return f"{self.prpject} - {self.name}"
