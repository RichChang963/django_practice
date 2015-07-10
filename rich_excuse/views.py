from django.shortcuts import render
from django.http import HttpResponse
from rich_excuse.models import Excuse

def home(request):
    	excuse = Excuse.objects.all().order_by('?')[0]
	return render(request, "index.html", {'excuse': excuse})