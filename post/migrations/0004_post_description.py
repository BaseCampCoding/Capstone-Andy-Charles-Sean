# Generated by Django 3.2.5 on 2021-07-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='Description', max_length=200),
        ),
    ]
