from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('createpost/', views.create_post, name='create_post'),
    path('editpost/<post_id>', views.edit_post, name='edit_post'),
    path('delete/<post_id>',views.delete_post,name='delete_post'),
    path('profile/<username>', views.get_user_profile, name='user_profile'),
    path('<slug:slug>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
