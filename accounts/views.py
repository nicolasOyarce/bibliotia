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
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.http import HttpResponse

from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account
from cart.models import Cart, CartItem
from cart.views import _cart_id
from orders.models import Order, OrderProduct


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
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_items = CartItem.objects.filter(cart=cart)
                
                    for item in cart_items:
                        item.user = user
                        item.save()
            except:
                pass

            auth.login(request, user)
            messages.success(request, 'Bienvenido, has iniciado sesion correctamente')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Credenciales invalidas', extra_tags='danger')
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
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    return render(request, 'accounts/dashboard.html',{
        'orders_count': orders_count,
    })

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
        messages.error(request, 'Link de activacion invalido', extra_tags='danger')
        return redirect('accounts:register')
    
def forgot_password(request):
    """
    View for the forgot password page
    """
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Restablecer contraseña'
            message = render_to_string('accounts/user/reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Se ha enviado un correo electronico con instrucciones para restablecer tu contraseña')
            return redirect('accounts:login')
        else:
            messages.error(request, 'La cuenta no existe', extra_tags='danger')
            return redirect('accounts:forgot_password')
    return render(request, 'accounts/user/forgot_password.html')

def reset_password_validate(request, uidb64, token):
    """
    View for the reset password validation page
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Por favor, restablece tu contraseña')
        return redirect('accounts:reset_password')
    else:
        messages.error(request, 'Este link a expirado', extra_tags='danger')
        return redirect('accounts:login')
    
def reset_password(request):
    """
    View for the reset password page
    """
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Contraseña restablecida correctamente')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Las contraseñas no coinciden', extra_tags='danger')
            return redirect('accounts:reset_password')
    else:
        return render(request, 'accounts/user/reset_password.html')
    
@login_required
def my_orders(request):
    """
    View for the my orders page
    """
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    return render(request, 'accounts/user/my_orders.html', {
        'orders': orders
    
    })

@login_required
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    return render(request, 'accounts/user/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password updated successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Please enter valid current password')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'accounts/user/change_password.html')


@login_required
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity

    return render(request, 'accounts/user/order_detail.html',{
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal
    })