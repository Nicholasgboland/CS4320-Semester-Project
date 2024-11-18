from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'test.html')
def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties_list.html', {'properties':properties})

def createProperty(request):
    if request.method == 'POST':
        form = Propertyform(request.POST)
        if form.is_valid():
            property = form.save(commit=False)  
            
            property.save()  
            return redirect('properties_list')
    else:
        form = Propertyform()  
    
    context = {'form': form}
    return render(request, 'create_property.html', context)