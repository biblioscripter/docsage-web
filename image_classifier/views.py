from django.shortcuts import render, redirect
from .forms import UserForm
from supabase import create_client, Client
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def get_supabase_client() -> Client:
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_KEY
    return create_client(url, key)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            supabase = get_supabase_client()
            supabase.table('users').insert({'username': username, 'password': password}).execute()
            
            return redirect('display_users')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def display_users(request):
    supabase = get_supabase_client()
    response = supabase.table('users').select('*').execute()
    users = response.data
    return render(request, 'display_users.html', {'users': users})