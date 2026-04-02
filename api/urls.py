from django.urls import path
from . import views 
# urlpatterns = [
#     path('public/', PublicView.as_view(), name='public-view'),     #Allowany
#     path('private/', PrivateView.as_view(), name='private-view'),  #Authenticate only 
# ]

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),

]
