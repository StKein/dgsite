# Generated by Django 3.0.6 on 2020-06-03 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200603_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
    ]