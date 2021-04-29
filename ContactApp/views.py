from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
#from django.core.mail import send_mail
#from django.conf import settings

# Create your views here.
'''
def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            topic = "no sé"
            message = request.POST.get("content") + " " + request.POST.get("email")
            email = settings.EMAIL_HOST_USER
            recipient_list = ["aplidinio@gmail.com"]

            send_mail(topic, message, email, recipient_list)
            try:
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?notvalid")

    return render(request, "ContactApp/contact.html", {'myform': contact_form})

'''
def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage("Message from App Django", "The user with name {} with adress {} writes the following: \n\n {}".format(name, email, content), "", ["aplidinio@gmail.com"], reply_to = [email])

            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?notvalid")

    return render(request, "ContactApp/contact.html", {'myform': contact_form})
