# Generated by Django 4.1.3 on 2023-02-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.TextField()),
                ('image_name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('slug', models.SlugField(blank=True, default='')),
                ('content', models.TextField()),
            ],
        ),
    ]
