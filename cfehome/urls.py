"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#from acx.views import account_create_view
from pages.views import home_view, contact_view, catalogue_view
from products.views import product_list_view, create_order_view, order_item_view, order_history_view, PriceView
from todoapi.views import TodoApiView
from image_app.views import product_image_view, success
from acx.views import registerPage, loginPage, logoutUser

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/',contact_view),
    path('catalogue/',catalogue_view),
    path('product/', product_list_view, name='product'),
    path('orders/', order_history_view.as_view(), name='orders'),
    path('register', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name="logout"),
    path('create-rental/', order_item_view, name='create-rental'),
    path('create-order/', create_order_view, name='create-order'),
    path('quote/', PriceView, name='quote' ),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', include('todoapi.urls')),
    path('image_upload', product_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)


#(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^' + settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})