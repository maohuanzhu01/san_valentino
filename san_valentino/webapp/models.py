from django.db import models

class DateCounter(models.Model):
    start_date = models.DateField()
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def days_passed(self):
        from datetime import date
        today = date.today()
        delta = today - self.start_date
        return delta.days

    def __str__(self):
        return f"{self.description}: {self.start_date}"
    

class Message(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


