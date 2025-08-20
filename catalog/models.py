from django.db import models

# Create your models here.
NA = 'N/A'

class CatalogBook(models.Model):
    author = models.CharField(max_length=200, blank=True, default=NA)
    title = models.CharField(max_length=200, unique=True)
    seria = models.CharField(max_length=200, blank=True, default=NA)
    pages_count = models.PositiveSmallIntegerField(blank=True, default=NA)
    year = models.PositiveSmallIntegerField(blank=True, default=0)
    language = models.CharField(max_length=200, blank=True, default=NA)
    isbn = models.CharField(max_length=13, unique=True, primary_key=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Catalog book'
        verbose_name_plural = 'Catalog books'

    def __str__(self):
        return f"{self.title}, ISBN: {self.isbn}"
