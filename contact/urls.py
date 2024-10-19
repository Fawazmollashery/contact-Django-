from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # List and search contacts
    path('add/', views.add_contact, name='add_contact'),  # Add a new contact
    path('update/<int:pk>/', views.update_contact, name='update_contact'),  # Update contact details
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),  # Delete a contact
]
