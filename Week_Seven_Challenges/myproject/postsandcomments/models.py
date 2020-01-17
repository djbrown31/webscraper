from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"ID: {self.id} Post Text: {self.post_text}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    
    def __str__(self):
        return f"ID: {self.id} Comment Text: {self.comment_text}"
    


