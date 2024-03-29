from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('courses.api.urls', namespace='api')),
    path('courses/', include('courses.urls'), name='courses'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
