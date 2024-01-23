from django.db import models


# Create your models here.
class Book(models.Model):
        desc = models.CharField(max_length=50,null=True,blank=True)
        Name = models.CharField(max_length=50, null=False)
        pub_year = models.DateTimeField()
        added_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
           return self.desc + self.Name