# Generated by Django 3.2.5 on 2021-07-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_address_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
