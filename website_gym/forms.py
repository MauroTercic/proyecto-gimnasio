from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import DatosPersonales

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = { 'username': None, 'email': None, 'password1': None, 'password2': None }
		
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Tu usuario'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



class EditarDatos(forms.ModelForm):
    nombre = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Nombre")
    apellido = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Apellido")
    peso = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Peso")
    masa = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Masa")
    grasa = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Grasa")
    cintura = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Cintura")
    brazo = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Brazo")
    pierna = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Pierna")
    pecho = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Pecho")
    pecho_respirado = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Pecho respirado")
    brazo_trabado = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Brazo trabado")
    altura = forms.FloatField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control", 'step': "0.01"}), label="Altura")
    edad = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"class":"form-control"}), label="Edad")


    class Meta:
        model = DatosPersonales
        exclude = ('usuario', 'created_at',)