from django.db import models

from users.models import User


class Message(models.Model):
    '''Модель сообщения'''
    subject_of_letter = models.CharField(max_length=100, verbose_name="Тема письма")
    body_of_letter = models.TextField(verbose_name='Тело письма')
    creator = models.ForeignKey(User, verbose_name='Создатель сообщения', on_delete=models.SET_NULL,
                                related_name="creator_message", null=True, blank=True)


class Client(models.Model):
    '''Модель клиент сервиса (получают рассылки)'''
    name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    email = models.EmailField(unique=True, verbose_name='Email')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    '''Модель рассылки писем'''
    FREQUENCY_CHOICES = [
        ('ежедневно', 'Один раз в день'),
        ('еженедельно', 'Раз в неделю'),
        ('ежемесячно', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('создано', 'Создано'),
        ('в процессе', 'В процессе'),
        ('завершено', 'Завершено'),
    ]
    start_datetime = models.DateTimeField(verbose_name='Дата и время начала')
    end_datetime = models.DateTimeField(verbose_name='Дата и время окончания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время первой отправки рассылки')
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(choices=STATUS_CHOICES, default='Созданный', verbose_name='Статус рассылки')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, verbose_name='Название компании')
    email = models.ManyToManyField(Client, verbose_name='Почта клиента')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name="Сообщение рассылки",
                                null=True, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingAttempt(models.Model):
    '''Модель попытки рассылки'''
    date_and_time = models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Связь рассылки и информации о её '
                                                                                'статусе')
    attempt_status = models.TextField(verbose_name='статус попытки(успешно/не успешно)')

    def __str__(self):
        return self.attempt_status

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
