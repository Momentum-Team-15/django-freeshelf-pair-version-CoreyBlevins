# Generated by Django 4.1.2 on 2022-10-26 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0005_category_resource_delete_categories_delete_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='freeshelf.category'),
        ),
    ]
