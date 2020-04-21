from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('StuReg_Form/',views.StuReg_Form,name='StuReg_Form'),
    path('All_Data/',views.All_Data,name='All_Data'),

]
