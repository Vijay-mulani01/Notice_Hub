from django.db import models

class Notice(models.Model):
    Subject=models.CharField(max_length=250)
    Description=models.TextField()
    Date_Posted=models.DateTimeField(auto_now_add=True)
    Date_Updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Notice'