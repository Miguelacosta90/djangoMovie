from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name = "Miguel", last_name = "Acosta")
    people = People.objects.all()
    print (people)
    return render(request,"movieTwo/index.html")
