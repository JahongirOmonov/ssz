from django.db import models
from datetime import datetime

# Create your models here.

class todoModel(models.Model):
    task_name = models.CharField(max_length=25, default='')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.task_name
    
    class Meta:
        db_table = 'todo'
