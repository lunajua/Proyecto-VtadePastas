from django.urls import path
from .views import RegisterView, Logout, Login


app_name = 'usuarios'

urlpatterns = [path('registro/',RegisterView.as_view(),name="registro"),
               path('logout/',Logout.as_view(), name="logout"),
               path('login/',Login.as_view(), name='login'),
               ]