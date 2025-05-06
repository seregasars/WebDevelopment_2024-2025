from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'rows': 5}))

