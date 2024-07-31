import email.message
import email.utils
import imaplib
import email
from email.header import decode_header

from django.utils import timezone

from mail_service.models import EmailMessage


class MailService:
    def __init__(self, email_account):
        self.email_account = email_account
        self.mail = imaplib.IMAP4_SSL(self.get_imap_server())
        self.mail.login(email_account.email, email_account.password)

    def get_imap_server(self):
        domain = self.email_account.email.split('@')[1]
        if domain == 'gmail.com':
            return 'imap.gmail.com'
        elif domain == 'yandex.ru':
            return 'imap.yandex.ru'
        elif domain == 'mail.ru':
            return 'imap.mail.ru'
        else:
            raise ValueError('Unsupported email domain')

    def fetch_messages(self):
        self.mail.select('inbox')
        status, messages = self.mail.search(None, 'ALL')
        email_ids = messages[0].split()
        for email_id in email_ids:
            status, msg_data = self.mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            subject, encoding = decode_header(msg['Subject'])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else 'utf-8')
            sent_date = email.utils.parsedate_to_datetime(msg['Date'])
            received_date = timezone.now()

            body = ''
            if msg.is_multipart():
                for part in msg.walk():
                    try:
                        body = part.get_payload(decode=True).decode()
                    except UnicodeDecodeError:
                        body = None
            else:
                try:
                    body = msg.get_payload(decode=True).decode()
                except UnicodeDecodeError:
                    body = None

            EmailMessage.objects.create(
                email_account=self.email_account,
                subject=subject,
                sent_date=sent_date,
                received_date=received_date,
                body=body,
                attachments=[]
            )
