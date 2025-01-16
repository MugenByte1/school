from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

def contact_view(request):
    contact = Contact.objects.first()
    return render(request, 'contact/contact.html', {'contact': contact})

def contact_edit(request):
    contact = Contact.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:contact')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_form.html', {'form': form})
