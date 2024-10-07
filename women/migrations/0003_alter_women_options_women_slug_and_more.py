# Generated by Django 5.1.1 on 2024-10-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_rename_model_women'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['-time_create'], name='women_women_time_cr_9f33c2_idx'),
        ),
    ]