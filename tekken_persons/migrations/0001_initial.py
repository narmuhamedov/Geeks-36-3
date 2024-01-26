# Generated by Django 3.2.5 on 2024-01-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Укажите имя персонажа')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите почту')),
                ('age', models.PositiveIntegerField(default=15, verbose_name='Укажите возраст персонажа')),
                ('image', models.URLField(verbose_name='Вставьте ссылку на фото')),
                ('capabilities', models.CharField(max_length=100, verbose_name='Укажите способность персонажа')),
                ('sport', models.CharField(choices=[('Каратэ', 'Каратэ'), ('Кунг-фу', 'Кунг-фу'), ('Муай-Тай', 'Муай-Тай'), ('Бокс', 'Бокс'), ('Кикбоксинг', 'Кикбоксинг'), ('Рестлинг', 'Рестлинг'), ('Нинзитцу', 'Нинзитцу')], max_length=100, verbose_name='Выберите спорт персонажа')),
                ('video_url', models.URLField(verbose_name='Вставьте ссылку с ютуб')),
            ],
        ),
    ]