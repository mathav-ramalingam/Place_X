# Generated by Django 5.1.6 on 2025-04-27 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('tenth_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('twelfth_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('diploma_status', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('pg_status', models.CharField(blank=True, max_length=100, null=True)),
                ('backlogs_history', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('current_backlogs', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='accounts.userregister')),
            ],
        ),
    ]
