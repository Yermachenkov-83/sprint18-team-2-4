from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('books/', include('book.urls')),
    path('authors/', include('author.urls')),
    path('orders/', include('order.urls')),
    path('api/v1/user', include('authentication.urls')),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/author/', include('author.urls')),
    path('api/v1/order/', include('order.urls')),
]
