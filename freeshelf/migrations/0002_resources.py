# Generated by Django 4.1.2 on 2022-10-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]