import os

from django.core.mail import send_mail




class MailSender:
    def send_email(self, instance):
        # send email using the self.cleaned_data dictionary
        clean_first_name = instance.cleaned_data['first_name']
        clean_last_name = instance.cleaned_data['last_name']
        clean_username = instance.cleaned_data['username']
        clean_email = instance.cleaned_data['email']
        message = "Phone: " + str(clean_first_name) + "\n" + "Email: " + clean_last_name + "\n" + "body: " + clean_username + clean_email
        print(message)
        #email_from = settings.EMAIL_HOST_USER
        #email_to = [os.environ.get('MY_EMAIL')]
        #send_mail(clean_email, message, email_from, email_to)
