"""
URL configuration for Task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.BMIview.as_view()),
    path('age/',views.Ageview.as_view()),
    path('percentage/',views.Percentageview.as_view()),
    path('simple-intrest/',views.Simpleintrestview.as_view()),
    path('electricity-bill/',views.ElectricityBillView.as_view()),
    path('discount/',views.DiscountView.as_view()),
    path('profit/',views.Profitview.as_view()),
    path('salary/',views.Salaryview.as_view()),
    path('time/',views.Timeview.as_view()),
    path('fuel-cost/',views.Fuelview.as_view()),
    path('product-profit/',views.Productview.as_view()),
    path('work-salary/',views.Worksalaryview.as_view()),
    path('age-details/',views.AgeDetailsview.as_view()),
]