"""p2_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import home, form, create, view, edit, update, delete, json, json_txt, login, cadastro_form, create_cadastro, update_cadastro, sobre, form_proprietarios, index_proprietarios, create_proprietarios, edit_proprietarios, view_proprietarios, update_proprietarios, delete_proprietarios, import_residencia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('cadastro_form', cadastro_form, name='cadastro_form'),
    path('create_cadastro/', create_cadastro, name='create_cadastro'),
    path('update_cadastro/<int:pk>/', update_cadastro, name='update_cadastro'),
    path('sobre', sobre, name='sobre'),

    path('index_proprietarios', index_proprietarios, name='index_proprietarios'),
    path('form_proprietarios/', form_proprietarios, name='form_proprietarios'),
    path('create_proprietarios/', create_proprietarios, name='create_proprietarios'),
    path('view_proprietarios/<int:pk>/', view_proprietarios, name='view_proprietarios'),
    path('edit_proprietarios/<int:pk>/', edit_proprietarios, name='edit_proprietarios'),
    path('update_proprietarios/<int:pk>/', update_proprietarios, name='update_proprietarios'),
    path('delete_proprietarios/<int:pk>/', delete_proprietarios, name='delete_proprietarios'),

    path('home', home, name='home'),
    path('json', json, name='json'),
    path('json_txt', json_txt, name='json_txt'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

    path('import_residencia', import_residencia, name='import_residencia'),
]
