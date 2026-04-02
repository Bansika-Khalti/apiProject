from django.urls import path
from .views import PublicView, PrivateView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public-view'),     #Allowany
    path('private/', PrivateView.as_view(), name='private-view'),  #Authenticate only 
]