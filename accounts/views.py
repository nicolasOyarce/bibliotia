from django.shortcuts import render

def register(request):
    """
    View for the register page
    """
    return render(request, 'accounts/register.html')