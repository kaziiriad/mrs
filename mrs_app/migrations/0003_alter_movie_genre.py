# Generated by Django 5.0.3 on 2024-04-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrs_app', '0002_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Romantic', 'Romantic'), ('Crime', 'Crime'), ('Thriller', 'Thriller')], max_length=50, null=True),
        ),
    ]
