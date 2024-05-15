# Generated by Django 5.0.3 on 2024-05-06 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
                ('category', models.CharField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')], default='General', max_length=100)),
                ('author', models.ForeignKey(limit_choices_to={'user_type': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
            ],
        ),
    ]