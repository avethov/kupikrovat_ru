"""kupikrovat_ru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
import src.apps.catalogue.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sale/', src.apps.catalogue.views.sale, name='sale'),
    url(r'^beds/', src.apps.catalogue.views.beds, name='beds'),
    url(r'products/(?P<id>\d+)', src.apps.catalogue.views.product_details, name='details'),
    url(r'^$', src.apps.catalogue.views.home_page, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

