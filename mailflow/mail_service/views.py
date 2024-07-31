from django.shortcuts import render, redirect
from .models import EmailAccount, EmailMessage
from mail_service.mail_service import MailService


def fetch_emails(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        email_account = EmailAccount.objects.create(
            email=email, password=password
        )
        service = MailService(email_account)
        service.fetch_messages()
        return redirect('email_list')
    return render(request, 'fetch_emails.html')


def email_list(request):
    messages = EmailMessage.objects.all()
    return render(request, 'email_list.html', {'messages': messages})
