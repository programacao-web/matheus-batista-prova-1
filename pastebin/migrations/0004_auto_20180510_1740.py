# Generated by Django 2.0.5 on 2018-05-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0003_auto_20180510_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='code',
            field=models.TextField(max_length=2000, verbose_name='Código'),
        ),
    ]
