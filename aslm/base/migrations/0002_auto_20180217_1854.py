# Generated by Django 2.0.2 on 2018-02-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
