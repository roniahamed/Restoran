from django.shortcuts import render
from .models import Item
from django.views.generic import ListView
# Create your views here.

def show(request):

    return render(request, 'items/index.html')


class ItemViews(ListView):
    model = Item
    template_name = 'items/data-show.html'
    context_object_name = 'items'