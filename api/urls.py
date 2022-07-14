import imp
from django.contrib import admin
from django.urls import include, path
from PetstoreDj import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('PetsoreDj.urls'))),
    
    
]