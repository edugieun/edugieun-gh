from django.db import models

# Create your models here.

class Algorithm(models.Model):
    prob_num = models.IntegerField()
    prob_source = models.CharField(max_length=10)
    prob_name = models.CharField(max_length=30)
    prob_diff = models.CharField(max_length=5)
    prob_category = models.CharField(max_length=20)
    code_url = models.TextField()
    
    def __str__(self):
        return self.prob_name

        #comment