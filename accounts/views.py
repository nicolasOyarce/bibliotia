from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse

from .forms import RegistrationForm
from .models import Account


def register(request):
    """
    View for the register page
    """
    if request.method == 'POST':
        # Get form values
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                username=username, 
                password=password)
            user.phone_number = phone_number
            user.save() 

            # User activation
            current_site = get_current_site(request)
            mail_subject = 'Por favor, activa tu cuenta'
            message = render_to_string('accounts/user/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            redirect_url = reverse('accounts:login') + '?command=verification&email=' + email
            return redirect(redirect_url)

        
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {
        'form': form
    
    })

def login_view(request):
    """
    View for the login page
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credenciales invalidas')
            return redirect('accounts:login')
        
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    """
    View for the logout page
    """
    auth.logout(request)
    messages.success(request, 'Sesion cerrada')
    return redirect('accounts:login')

@login_required
def dashboard(request):
    """
    View for the dashboard page
    """
    return render(request, 'accounts/dashboard.html')

def activate(request, uidb64, token):
    """
    View for the activation page
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Felicidades!!!, tu cuenta a sido activada')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Link de activacion invalido')
        return redirect('accounts:register')