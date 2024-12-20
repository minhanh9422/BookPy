from django.db import models

# Create your models here.
class Book(models.Model):
    bid=models.CharField(max_length=10)
    btittle=models.CharField(max_length=20)
    bauthor=models.CharField(max_length=100)
    # bgenres=models.CharField(max_length=20)
    # bcover=models.CharField()
    # bimg_cover=models.CharField(max_length=20)
    # bdescription=models.CharField(max_length=20)
    class Meta:
        db_table = "book"