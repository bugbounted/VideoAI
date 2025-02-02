from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from VideoAI.views import templates_view, text_input_view, text_view, image_view, register_request, login_request, upload_image
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('VideoAI/', text_input_view, name='text-input'),
    path('VideoAI/textview/', text_view, name='text-view'),
    path('VideoAI/src/images/', image_view, name='image-view'),
    path('VideoAI/src/templates/', templates_view, name='template-view'),
    path('register/', register_request, name ='register'),
    path("login/", login_request, name="login"), 
    path("VideoAI/addimage/", upload_image, name="add-image"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)