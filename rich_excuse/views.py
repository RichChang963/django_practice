from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    rich_excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    return HttpResponse(rich_excuses[0])