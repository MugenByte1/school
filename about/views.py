from django.shortcuts import render, redirect
from .models import About
from django.contrib.auth.decorators import login_required
from .forms import AboutForm

def about_view(request):
    about = About.objects.first()
    return render(request, 'about/about.html', {'about': about})

@login_required
def about_edit(request):
    about = About.objects.first()
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about:about')
    else:
        form = AboutForm(instance=about)
    return render(request, 'about/about_form.html', {'form': form})
