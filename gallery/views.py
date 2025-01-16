from django.shortcuts import render, redirect
from .models import GalleryItem
from django.contrib.auth.decorators import login_required
from .forms import GalleryItemForm

def gallery_list(request):
    items = GalleryItem.objects.all()
    return render(request, 'gallery/gallery_list.html', {'items': items})

def gallery_add(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_list')
    else:
        form = GalleryItemForm()
    return render(request, 'gallery/gallery_form.html', {'form': form})

def gallery_edit(request, pk):
    item = GalleryItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_list')
    else:
        form = GalleryItemForm(instance=item)
    return render(request, 'gallery/gallery_form.html', {'form': form})

def gallery_delete(request, pk):
    item = GalleryItem.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('gallery:gallery_list')
    return render(request, 'gallery/gallery_confirm_delete.html', {'item': item})
