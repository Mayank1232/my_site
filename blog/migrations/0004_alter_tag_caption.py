# Generated by Django 4.1.3 on 2023-02-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='caption',
            field=models.CharField(max_length=100),
        ),
    ]
