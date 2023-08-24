from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("basic",views.basi,name='BasicPlan'),
    path("inter",views.inter,name='IntermediatePlan'),
    path("premium",views.premiu,name='PremiumPlan'),
    path("portfolio",views.pofo,name='portfolio')
]