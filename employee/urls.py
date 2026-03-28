from django.urls import include, path

from . import views

urlpatterns = [
    path('add/', views.add_employee, name="add_employee"),
    path('get/', views.get_employees, name="get_employees"),
    path('update/<int:id>/', views.update_employee, name="update_employee"),
    path('delete/<int:id>/', views.delete_employee, name="delete_employee"),
]