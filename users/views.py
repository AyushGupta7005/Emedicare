from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'user.html',{'form':form})