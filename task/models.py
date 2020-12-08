from django.db import models

# Create your models here.

class Task(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"
    choices = [
        ('Pending','Pending'),
        ('Completed', 'Completed')
    ]
    task                = models.CharField(max_length=50)
    details             = models.TextField(blank=True, null=True)
    start_date          = models.DateField(auto_now=False, auto_now_add=False)
    end_date            = models.DateField(blank=True, null=True)
    status              = models.CharField(default='Pending',choices=choices,max_length=50)
    created_at          = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task
