from django.shortcuts import render
from .forms import ContactForm

def home(request):

    context={'title':'home page'}
    return render(request,'home.html',context)


def about(request):
    context={'title':'about page'}
    return render(request,'home.html',context)


def contact(request):
    contact_form=ContactForm(request.POST or None)

    context={'title':'contact page',
             'form':contact_form}

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'home.html',context)