"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import TaskIndexView, TaskView, TaskCreateView, DeleteView, TaskUpdateView,\
    ProjectIndexView, ProjectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskIndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='view'),
    path('task/add/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='update'),
    path('projects/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view')
]
