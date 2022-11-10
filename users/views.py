from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views.generic import ListView
from storage.models import AiModel
# Create your views here.

def index(request):
    return render(request,'users/index.html')


class DashboardListView(ListView):
    model = AiModel
    template_name = "users/dashboard.html"
    paginate_by = 10

def register(request):
    if request.method=='GET':
        return render(request,'users/register.html',{'form' :CustomUserCreationForm})
    elif request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.backend="django.contrib.auth.backends.Modelbackend"
            user.save()
            login(request,user)
            return redirect(reverse('dashboard'))
        
        
def about(request):
    return render(request,'users/about.html')


def team(request):
    return render(request,'users/team.html')

        
# def contact(request):
#     return render(request,'users/contact.html')




         
