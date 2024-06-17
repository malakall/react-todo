from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250) # в чар филд максимум 250 символов а в текст филд 15000
    full_text = models.TextField('статья')
    date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.title  # этот метод необходим для красивого вывода новостей
    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'новости' # добавляем название в множественной форме
