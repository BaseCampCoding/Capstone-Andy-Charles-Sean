# Generated by Django 3.2.5 on 2021-07-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_merge_20210728_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
