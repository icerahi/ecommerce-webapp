from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    context={'title':'home page'}
    return render(request,'home.html',context)
def about(request):
    context={'title':'about page'}
    return render(request,'about.html',context)


def contact(request):

    contact_form=ContactForm()

    if request.method=='POST':

        contact_form=ContactForm(request.POST)
        print(request.POST)

        if contact_form.is_valid():

             print(contact_form.cleaned_data['email'])


             return redirect('home')

    return render(request,'contact.html',{'form':contact_form})




def login(request):
    return render(request,'login.html',{})

