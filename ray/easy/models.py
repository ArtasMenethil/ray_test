from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Заголовок')
    author = models.CharField(max_length=50, blank=True, null=True, verbose_name='Автор')
    source = models.CharField(max_length=50, blank=True, null=True, verbose_name='Портал')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.id
