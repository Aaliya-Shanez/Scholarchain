# Generated by Django 4.0.1 on 2024-03-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scholarchain', '0005_scholarship_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Required_Sponsorship',
            field=models.CharField(default='No', max_length=20),
        ),
    ]
