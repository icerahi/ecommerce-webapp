from django import forms
class ContactForm(forms.Form):
    fullname=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Full Name',
        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Email Address',
        }
    ))
    content=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Your Message here'
        }
    ))