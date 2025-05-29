"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
## custom imports
from home.views import home, successPageFromHome
from vege.views import receipes, delete_receipe, update_receipe, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    ###
    path('', home, name='home'),
    path('success/', successPageFromHome, name='success_page_from_home'),
    ## receipes view
    path('receipes/', receipes, name='receipes'),
    path('delete-receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update-receipe/<int:id>/', update_receipe, name='update_receipe'),
    ## login page
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),  # Assuming the same view handles registration
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
