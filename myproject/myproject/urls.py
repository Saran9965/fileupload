from django.contrib import admin
from django.urls import path
from uploadfiles import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('uploadfile',views.uploadfile,name='uploadfile'),
    path('deletefile/<int:id>',views.deletefile,name='deletefile'),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

