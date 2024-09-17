from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import ShortURL
from .forms import URLForm
import random
import string

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generate_short_url()
            ShortURL.objects.create(original_url=original_url, short_url=short_url)
            
            return render(request, 'urlcreated.html', {'short_url': short_url ,'obj': original_url})
    else:
        form = URLForm()
    return render(request, 'home.html', {'form': form})

def redirect_to_url(request, short_url):
    try:
        url_mapping = ShortURL.objects.get(short_url=short_url)
        return redirect(url_mapping.original_url)
    except ShortURL.DoesNotExist:
        return HttpResponseNotFound('URL not found')