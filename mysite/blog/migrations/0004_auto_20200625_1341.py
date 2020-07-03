# Generated by Django 3.0.7 on 2020-06-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200622_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
