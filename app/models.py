from django.db import models


class Event(models.Model):
    name=models.CharField(max_length=100)
    detail=models.CharField(max_length=1000)
    datetime=models.DateTimeField()
    location=models.CharField(max_length=200)

    def ____(self):
        return f"name: {self.name}, detail:{self.detail}, datetime:{self.datetime}, location:{self.location}"


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True) # what is the benefit of blank=True?
    events=models.ManyToManyField(Event)

    def ____(self):
        return f"name:{self.name}, age:{self.age}, email:{self.email}"
