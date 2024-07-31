from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from mail_service.mail_service import MailService
from mail_service.models import EmailAccount


@shared_task
def fetch_emails_task(email_account_id):
    email_account = EmailAccount.objects.get(id=email_account_id)
    service = MailService(email_account)
    messages = service.fetch_messages()
    channel_layer = get_channel_layer()

    for i, message in enumerate(messages):
        progress = (i + 1) / len(messages) * 100
        async_to_sync(channel_layer.group_send)(
            'progress',
            {
                'type': 'send_progress',
                'progress': progress,
                'message': message
            }
        )
