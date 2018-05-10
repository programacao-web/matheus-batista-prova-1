from django.db import models
from pygments.lexers import get_all_lexers

LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in get_all_lexers() if item[1]])


class Paste(models.Model):
    title = models.CharField(max_length=10, verbose_name="Título")
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=15, verbose_name="Linguagem")
    code = models.TextField(max_length=2000, verbose_name="Código")

