# Generated by Django 3.0.7 on 2020-06-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200621_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
