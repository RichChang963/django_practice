from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    rich_excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    excuse = random.choice(rich_excuses)
    return render(request, "index.html", {'excuse': excuse.upper()})