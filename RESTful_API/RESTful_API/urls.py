from django.contrib import admin
from django.conf.urls import url
from app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('employees/', views.employeeList.as_view()),
]
