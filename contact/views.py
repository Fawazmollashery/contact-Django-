from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

# View all contacts
def contact_list(request):
    query = request.GET.get('search', '')
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts, 'query': query})

# Add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# Update contact details
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form': form, 'contact': contact})

# Delete a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_contact.html', {'contact': contact})
