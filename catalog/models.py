from django.db import models

# Create your models here.
NA = 'N/A'


class CatalogBook(models.Model):
    author = models.CharField(
        max_length=200,
        blank=True,
        default=NA,
        help_text='Enter author name')
    title = models.CharField(
        max_length=200,
        unique=True,
        help_text='Enter book title')
    seria = models.CharField(
        max_length=200,
        blank=True,
        default=NA,
        help_text='Enter book seria')
    pages_count = models.PositiveSmallIntegerField(
        blank=True,
        default=NA,
        help_text='Enter book pages count')
    year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text='Enter book year')
    language = models.CharField(
        max_length=200,
        blank=True,
        default=NA,
        help_text='Enter number of the pages in book')
    isbn = models.CharField(
        max_length=13,
        unique=True,
        primary_key=True,
        help_text='Enter book ISBN')

    class Meta:
        ordering = ['title']
        verbose_name = 'Catalog book'
        verbose_name_plural = 'Catalog books'

    def __str__(self):
        return f"{self.title}, ISBN: {self.isbn}"
