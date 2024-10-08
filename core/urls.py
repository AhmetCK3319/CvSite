from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.get_cv, name="get_cv"),
    path("contact_message", views.contact_message, name="contact_message"),
]
