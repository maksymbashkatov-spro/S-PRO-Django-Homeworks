from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('bookstore/', include('bookstore.urls')),
    path('accounts', include('accounts.urls'))
]
