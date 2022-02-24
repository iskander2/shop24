import random
import string
from django.conf import settings
from django.core.mail import send_mail

def get_random_string():
    random_source = string.ascii_letters + string.digits
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    

    # generate other characters
    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

def send_auth_url(email,code):
    send_mail(
    'url avtorizaciya',
    settings.SITE_URL +'authe/code/' + code,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,

)

def send_change_url(email,message):
    send_mail(
    'url izmeneniya',
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
