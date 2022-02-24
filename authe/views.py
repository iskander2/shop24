from email import message
from django.shortcuts import render
from django.conf import settings
from .forms import UserRegistrationForm, EmailChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .utils import send_auth_url,send_change_url
from .models import ConfirmationCode
from django.shortcuts import get_object_or_404


User = get_user_model()
# Create your views here.

def registration(request):
    form = UserRegistrationForm(request.POST or None)
    message = False
    if request.method == 'POST' and form.is_valid():
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(email=email)
        user.set_password(password)
        user.save()
        code = ConfirmationCode.objects.create(user=user)
        send_auth_url(email = user.email,code=code.code)
        message = 'Вам отправили на почту'
        form = UserRegistrationForm()


    return render(request,'registration.html',{'form':form, 'message':message})


def account_confirm(request,code):
    code = get_object_or_404(ConfirmationCode,code=code)
    user = code.user
    user.verify = True
    user.save()
    return render(request,'success.html',{'message':'вы зарегались'})

def account(request):
    return render(request,'account.html')

def edit_request(request):
    change_field = request.GET.get('field')
    code =ConfirmationCode.objects.create(user=request.user)
    if change_field == 'password':
        url = settings.SITE_URL +'authe/password/' + code.code+"/"
        send_change_url(request.user.email,url)
        return render(request,'success.html',{'message':'отправлено на почту password'})    
    elif change_field == 'email':
        url = settings.SITE_URL +'authe/email/' + code.code+"/"
        send_change_url(request.user.email,url)
        return render(request,'success.html',{'message':'отправлено на почту email'})
    return render(request,'success.html',{'message':'что то пошло не так как надо'})
        
def change_email(request,code):
    code = get_object_or_404(ConfirmationCode,code=code)
    if code.confirm:
        return render(request,'success.html',{'message':'этот код уже потвержден'})
    form = EmailChangeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = request.POST.get('email')
        user = code.user
        user.verify = False
        user.email = email
        user.save()
        new_code = ConfirmationCode.objects.create(user=user)
        send_auth_url(email = user.email,code=new_code.code)
        code.confirm = True
        code.save()
        return render(request,'success.html',{'message':'код отправлен на новый email'})
    return render(request,'email.html',{'form':form})

def change_password(request,code):
    code = get_object_or_404(ConfirmationCode,code=code)
    if code.confirm:
        return render(request,'success.html',{'message':'этот код уже потвержден'})
    form = PasswordChangeForm(request.POST or None)    
    if request.method == "POST" and form.is_valid():
        password = request.POST.get('password')
        user = code.user
        user.set_password(password)
        user.save()
        return render(request,'success.html',{'message':'ваш пароль изменён'})
    return render(request,'email.html',{'form':form})    






        

            
        
    
    
     






    