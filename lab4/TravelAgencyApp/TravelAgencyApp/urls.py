from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel.urls', namespace='travel')),
    path('login/', include('login.urls', namespace='login')),
    path('order/', include('order.urls', namespace='order')),
]
