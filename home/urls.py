from django.urls import path
from . import views

urlpatterns = [
    #path("", views.home), #function based view
    path("", views.HomeView.as_view()), #for class based view 
    path("authorized", views.AuthorizedView.as_view())
]
