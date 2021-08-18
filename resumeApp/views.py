from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render


from resumeApp.forms import ContactForm
from resumeApp.signals import notify_me_by_mail
# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def post(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        
        if form.is_valid():
            # send signal to send a mail to me and
            notify_me_by_mail(sender=None, dispatch_uid="NotifyMe", form=form)
            return JsonResponse({"message": "Your messgae has be been delivered"})
        else:
            return JsonResponse(data=form.errors)

