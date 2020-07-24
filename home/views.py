from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'Home/home.html')