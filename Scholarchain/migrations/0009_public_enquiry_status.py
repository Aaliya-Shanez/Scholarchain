# Generated by Django 4.0.1 on 2024-04-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scholarchain', '0008_addscholarships_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='public_enquiry',
            name='Status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]