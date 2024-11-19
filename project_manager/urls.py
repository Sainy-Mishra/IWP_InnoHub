# project_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from projects import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.project_list, name='project_list'),
    # Update the logout URL to use POST method
    path('logout/', LogoutView.as_view(next_page='project_list'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('submit/', views.submit_project, name='submit_project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]