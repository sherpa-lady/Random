# Generated by Django 3.0.7 on 2020-07-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Travel diaries', 'Travel diaries'), ('Achievement', 'Achievement'), ('college', 'college')], max_length=200, null=True),
        ),
    ]
