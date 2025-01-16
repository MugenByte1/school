from django.shortcuts import render, redirect
from .models import Colleague
from django.contrib.auth.decorators import login_required
from .forms import ColleagueForm

def colleagues_list(request):
    colleagues = Colleague.objects.all()
    return render(request, 'colleagues/colleagues_list.html', {'colleagues': colleagues})

def colleague_add(request):
    if request.method == 'POST':
        form = ColleagueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('colleagues:colleagues_list')
    else:
        form = ColleagueForm()
    return render(request, 'colleagues/colleague_form.html', {'form': form})

def colleague_edit(request, pk):
    colleague = Colleague.objects.get(pk=pk)
    if request.method == 'POST':
        form = ColleagueForm(request.POST, request.FILES, instance=colleague)
        if form.is_valid():
            form.save()
            return redirect('colleagues:colleagues_list')
    else:
        form = ColleagueForm(instance=colleague)
    return render(request, 'colleagues/colleague_form.html', {'form': form})

def colleague_delete(request, pk):
    colleague = Colleague.objects.get(pk=pk)
    if request.method == 'POST':
        colleague.delete()
        return redirect('colleagues:colleagues_list')
    return render(request, 'colleagues/colleague_confirm_delete.html', {'colleague': colleague})
