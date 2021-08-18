import os


from django.core.signals import request_finished
from django.core.mail import EmailMessage, BadHeaderError
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone

from HngTask1.settings import BASE_DIR

@receiver([request_finished])
def notify_me_by_mail(sender=None, **kwargs):
    uid = kwargs.get("dispatch_uid")
    if uid == "NotifyMe":
        my_email = os.environ.get("OWNER_EMAIL", os.getenv("OWNER_EMAIL"))
        form = kwargs.get("form")
        
        mail = EmailMessage(
            subject = "Resume Contact",
            body=build_message_from_form(form),
            to=[my_email]
        )
        
        delivered = False
        
        try:
            delivered = True if ( mail.send(fail_silently=False) == 1) else False
        except BadHeaderError: 
            pass

        return delivered



def build_message_from_form(form):
    msg_txt = ""
    path = f'{settings.BASE_DIR}/resumeApp/message.txt'

    with open(path, 'r') as template:
        msg_txt = template.read()
        fields = ["name", "email", "phone", "company", "message"]

        for field in fields:
            msg_txt = msg_txt.replace(f"{{{{ {field} }}}}", form.data.get(field))
        
        msg_txt = msg_txt.replace("{{ date }}", str(timezone.now()))
    print(msg_txt)

    return msg_txt