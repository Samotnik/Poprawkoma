from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import Zgloszenie
from .decorators import allowed_users
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('uczen_page')
        else:
            messages.info(request, "Nazwa użytkownika lub hasło jest źle")
    context = {'essa':"test"}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles='uczen')
def uczenPage(request):
  form1 = Zgloszenie
  subitted = False
  if request.method == 'POST':
        form = Zgloszenie(request.POST)
        if form.is_valid():
            user= request.user.uczen
            temat = form.cleaned_data.get('temat')
            przedmiot = form.cleaned_data.get('przedmiot')
            nauczyciel = form.cleaned_data.get('nauczyciel')
            data = form.cleaned_data.get('data')
            t = Poprawa(user1=user,temat= temat,przedmiot = przedmiot,nauczyciel = nauczyciel, data=data)
            t.save()
            import smtplib
            import ssl
            from email.message import EmailMessage

            email_sender = 'poprawkomat@gmail.com'
            email_password = 'fkuysyjdyzbofbto'
            email_receiver = request.user.email
            subject = temat
            body = """Temat: {}\n\nPrzedmiot: {}\n\nUczeń: {}\n\nData: {}""".format(temat, przedmiot, user, data)
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)


            context = ssl.create_default_context()


            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
        return HttpResponseRedirect('?subitted=True')
  po = Poprawa.objects.all()
  print(po)
  return render(request, 'uczen_strona.html', {"po":po,"form":form1})

def pomoc(request):
  return render(request, 'logowanie_pomoc.html', {})

@login_required(login_url='login')
@allowed_users(allowed_roles='nauczyciel')
def nauczycielPage(request):
  po = Poprawa.objects.all()

  return render(request, 'nauczyciel_page.html', {"po":po})
