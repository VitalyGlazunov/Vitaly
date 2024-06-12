from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):

    STATUS_BUG = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершен'),
    ]

    PRIORITIES_BUG = [
        ('One', 'Первый'),
        ('Two', 'Второй'),
        ('Three', 'Третий'),
        ('Four', 'Четвертый'),
        ('Five', 'Пятый'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(max_length=50, choices=STATUS_BUG, default='New')
    priority = models.CharField(max_length=50, choices=PRIORITIES_BUG)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    STATUS_REQUEST = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонение х2'),
    ]

    PRIORITIES_REQUEST = [
        ('One', 'Первый'),
        ('Two', 'Второй'),
        ('Three', 'Третий'),
        ('Four', 'Четвертый'),
        ('Five', 'Пятый'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(max_length=50, choices=STATUS_REQUEST, default='Рассмотрение')
    priority = models.CharField(max_length=50, choices=PRIORITIES_REQUEST)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
