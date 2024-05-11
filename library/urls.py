from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from books.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(),  name='login'),
    path('logout/', logout_view, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
