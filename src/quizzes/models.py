from django.db import models

class HighScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.score}"
    
class Quiz2HighScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.score}"
    
class Quiz3HighScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.score}"



