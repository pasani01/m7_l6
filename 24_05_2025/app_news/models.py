from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    views_count = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'news'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'