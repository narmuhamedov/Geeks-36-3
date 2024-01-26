from django.db import models


class PersonGame(models.Model):
    SPORT = (
        ('Каратэ', 'Каратэ'),
        ('Кунг-фу', 'Кунг-фу'),
        ('Муай-Тай', 'Муай-Тай'),
        ('Бокс', 'Бокс'),
        ('Кикбоксинг', 'Кикбоксинг'),
        ('Рестлинг', 'Рестлинг'),
        ('Нинзитцу', 'Нинзитцу')
    )
    name = models.CharField(max_length=30, null=True, verbose_name='Укажите имя персонажа')
    email = models.EmailField(verbose_name='Укажите почту', blank=True, null=True)
    description = models.TextField(verbose_name='Укажите описание', blank=True, null=True)
    age = models.PositiveIntegerField(default=15, verbose_name='Укажите возраст персонажа')
    image = models.URLField(verbose_name='Вставьте ссылку на фото')
    capabilities = models.CharField(max_length=100, verbose_name='Укажите способность персонажа')
    sport = models.CharField(max_length=100, choices=SPORT, verbose_name='Выберите спорт персонажа')
    video_url = models.URLField(verbose_name='Вставьте ссылку с ютуб')

    def __str__(self):
        return f'{self.name}-{self.sport}'

    class Meta:
        verbose_name = 'Персонажа'
        verbose_name_plural = 'Персонажи'


class Review(models.Model):
    tekken_person = models.ForeignKey(PersonGame, on_delete=models.CASCADE, related_name='tekken_reviews')
    text = models.TextField()

    def __str__(self):
        return self.text