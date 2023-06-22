from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def index(request):

    <html>
        <body>
        <h1>Bem vindo</h1>
        </body>
    </html>

    return HttpResponse(html)