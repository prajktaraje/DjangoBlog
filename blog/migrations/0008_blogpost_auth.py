# Generated by Django 3.1.4 on 2021-02-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210209_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='auth',
            field=models.CharField(default='', max_length=20),
        ),
    ]
