from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


