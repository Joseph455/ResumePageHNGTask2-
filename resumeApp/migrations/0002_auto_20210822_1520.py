# Generated by Django 3.0.9 on 2021-08-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]