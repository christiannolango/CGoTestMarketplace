from django.shortcuts import render, get_object_or_404
from .models import Item


#render marketplace index page with all items
def index(request):
    items = Item.objects.all()
    return render(request, 'marketplace/index.html', {
        'items': items,
    })

#render marketplace item detail page
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'marketplace/detail.html', {
        'item': item,
    })