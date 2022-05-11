from django.db import models
from django.urls import reverse
from accounts.models import User


class Notes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=150, blank=False, null=False)
    body = models.CharField(max_length=2000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Notes"

    def get_absolute_url(self):
        print(self.id)
        return reverse('author_notes_list')
