from django.db import models

# creating company model

class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('NON-IT', 'NON-IT'), ('Mobile', 'Mobile')))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name+"--"+self.locations
    


