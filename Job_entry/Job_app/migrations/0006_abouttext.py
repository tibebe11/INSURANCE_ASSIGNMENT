# Generated by Django 4.2.4 on 2023-08-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_1', models.ImageField(upload_to='about/')),
                ('image_2', models.ImageField(upload_to='about/')),
                ('image_3', models.ImageField(upload_to='about/')),
                ('description_2', models.TextField()),
                ('description_3', models.TextField()),
                ('point', models.CharField(max_length=255)),
            ],
        ),
    ]