# Generated by Django 4.0.1 on 2024-03-24 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scholarchain', '0004_alter_addscholarships_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('SCHOLARSHIPS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scholarchain.addscholarships')),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scholarchain.student')),
            ],
        ),
    ]