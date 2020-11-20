"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from foodconf.views import login_page
from django.conf import settings
from django.conf.urls.static import static
from doctors.views import profile_page ,get_dc_aptient ,patient_detail ,create_patient , create_tfhr,create_new_tfhr
urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^login/', login_page, name='login'),
      url(r'^profile/', profile_page, name='profile'),
      url(r'^patient_detail/(?P<patient_id>\d+)/$', patient_detail, name='patient_detail'),
       # url(r'^profile/(?P<user_id>\d+)/$' , profile_page,name='profile'),
       url(r'^patient/', get_dc_aptient, name='patient'),
        url(r'^create_patient/', create_patient, name='create_patient'),
        # url(r'^tfrc/(?P<p_id>\d+)/$', create_tfhr, name='tfrc'),
        url(r'^create-tfhr/(?P<p_id>\d+)/$', create_tfhr, name='create-tfhr'),
         url(r'^cntfhr/(?P<p_id>\d+)/$', create_new_tfhr, name='cntfhr'),
        # url(r'^tfrc/', create_tfhr, name='tfrc'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
