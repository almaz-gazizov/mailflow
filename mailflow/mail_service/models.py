from django.db import models

MAX_LENGTH = 255


class CreatedUpdatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class EmailAccount(CreatedUpdatedAt):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return self.email


class EmailMessage(CreatedUpdatedAt):
    email_account = models.ForeignKey(
        EmailAccount, on_delete=models.CASCADE, related_name='messages'
    )
    subject = models.CharField(max_length=MAX_LENGTH)
    sent_date = models.DateTimeField()
    received_date = models.DateTimeField()
    body = models.TextField()
    attachments = models.JSONField()

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return f'{self.email_account}: {self.subject}'
