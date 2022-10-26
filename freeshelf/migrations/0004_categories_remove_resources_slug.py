# Generated by Django 4.1.2 on 2022-10-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0003_resources_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='resources',
            name='slug',
        ),
    ]
