# Generated by Django 3.2.5 on 2024-01-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekken_persons', '0003_auto_20240119_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persongame',
            name='email',
        ),
        migrations.AddField(
            model_name='persongame',
            name='email1',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Укажите почту'),
        ),
    ]
