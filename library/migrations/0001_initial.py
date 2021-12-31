# Generated by Django 3.2.9 on 2021-12-30 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EBooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('abstract', models.TextField(max_length=1000)),
                ('file', models.FileField(upload_to='media/library', validators=[library.validators.validate_file_extension])),
                ('datePosted', models.DateField(auto_now_add=True, verbose_name='dd mm yyyy')),
                ('book_cover', models.ImageField(upload_to='media/news')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
