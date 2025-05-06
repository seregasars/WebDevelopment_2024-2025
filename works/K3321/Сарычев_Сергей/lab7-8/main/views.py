# main/views.py
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage  # Импортируем модель

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Сохраняем данные в базу данных
            ContactMessage.objects.create(name=name, email=email, message=message)

            # Отображаем страницу благодарности
            return render(request, 'main/thank_you.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
