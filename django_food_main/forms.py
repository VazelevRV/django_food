from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text', 'id': 'name', 'class': 'form-control', 'placeholder': 'Ім\'я', 'required': 'required'}))
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email',
                                                                'class': 'form-control', 'placeholder': 'example@gmail.com',
                                                                'required': 'required'}))
    message = forms.CharField(max_length=200,
                                   widget=forms.Textarea(
                                       attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
                                              'rows': '4', 'placeholder': 'Повідомлення',
                                              'required': 'required'}))

    class Meta:
        model = Reservation
        fields = ('user_name', 'user_email', 'message')
