from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views 
# urlpatterns = [
#     path('public/', PublicView.as_view(), name='public-view'),     #Allowany
#     path('private/', PrivateView.as_view(), name='private-view'),  #Authenticate only 
# ]

# urlpatterns = [
#     path('blogs/', views.blog_list, name='blog_list'),

# ]
urlpatterns =[
    path('gettoken/', obtain_auth_token, name='api_token_auth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('adminpanel/', views.admin_panel, name='admin_panel'),
]