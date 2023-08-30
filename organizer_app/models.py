from django.db import models
from django.contrib.auth.models import User
# 'content_id': response['d'][0]['id'],
#           'content_name': response['d'][0]['l'],
#           'content_image': response['d'][0]['i']['imageUrl'],
#           'content_type': response['d'][0]['qid'],
#           'release_year': response['d'][0]['y'],

class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    type = models.CharField(max_length=50)
    top_rank = models.IntegerField()
    image = models.URLField()
    duration = models.IntegerField()
    rating = models.FloatField()
    genres = models.JSONField()
    some_plot = models.TextField()
    full_plot = models.TextField()
    is_watched = models.BooleanField(default=False)
    def __str__(self):
        return self.title
