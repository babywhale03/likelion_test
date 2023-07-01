from django.db import models
from django.utils import timezone

class Club(models.Model):
    club_name = models.CharField(max_length = 30)
    introduction = models.CharField(max_length = 100)
    member = models.IntegerField()

    def __str__(self):
        return self.club_name
    
class Comment(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content