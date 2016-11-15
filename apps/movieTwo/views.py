from django.shortcuts import render
from .models import People
# Create your views here.
def index(requuest):
    people.objects.create(first_name="Miguel", last_name="Acosta")
    people = people.objects.all()
    print (people)
    render(request,"movieTwo/index.html")
