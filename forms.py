
#     all is data


from django import forms

from .models import form_1, form_2, form_3, form_5, verification0



class StudentRegistration(forms.ModelForm):
    class Meta:
        model = form_1
        fields = ['name', 'email', 'password', 'number', 'age', 'code']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class' : 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentRegistration2(forms.ModelForm):
    class Meta:
        model = form_2
        fields = ['name', 'email', 'password', 'state']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentRegistration3(forms.ModelForm):
    class Meta:
        model = form_3
        fields = ['jour', 'nom', 'sept_heure', 'huit_heure', 'neuf_heure', 'dix_heure', 'onze_heure', 'douze_heure', 'treize_heure', 'quatorze_heure', 'quinze_heure', 'seize_heure', 'dix_sept_heure', 'dix_huit_heure', 'dix_neuf_heure']
        widgets = {
            'jour' :    forms.TextInput(attrs={'class': 'form-control'}),
            'nom' :    forms.TextInput(attrs={'class': 'form-control'}),
            'sept_heure' :    forms.TextInput(attrs={'class': 'form-control'}),
            'huit_heure' :    forms.TextInput(attrs={'class': 'form-control'}),
            'neuf_heure' : forms.TextInput(attrs={'class': 'form-control'}),
            'dix_heure':     forms.TextInput(attrs={'class': 'form-control'}),
            'onze_heure':  forms.TextInput(attrs={'class': 'form-control'}),
            'douze_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'treize_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'quatorze_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'quinze_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'seize_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'dix_sept_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'dix_huit_heure':    forms.TextInput(attrs={'class': 'form-control'}),
            'dix_neuf_heure':    forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentRegistration5(forms.ModelForm):
    class Meta:
        model = form_5
        fields = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'occupate']
        widgets = {
            'lundi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'mardi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'mercredi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'jeudi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'vendredi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'samedi' :    forms.TextInput(attrs={'class': 'form-control'}),
            'occupate' :    forms.NumberInput(attrs={'class': 'form-control'}),
        }
        

class StudentRegistration4(forms.ModelForm):
    class Meta:
        model = verification0
        fields = ['jour_choisi']
        widgets = {
            'jour_choisi' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        