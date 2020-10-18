from django.conf.urls import url
from django.template.context_processors import static
from django.urls import re_path, path

from . import views

app_name='vendor_data_collection'

urlpatterns = [

    re_path('user/',views.index,name='add'),
    re_path('save/',views.save,name='save'),
    re_path('finalize/',views.finalize,name='finalize'),
    re_path('add/p1',views.add_vendor_p1,name='add-vendor-p1'),
    path('add/p2/',views.add_vendor_p2,name='add-vendor-p2'),
    path('add/p3/',views.add_vendor_p3,name='add-vendor-p3'),
    path('add/p4/',views.add_vendor_p4,name='add-vendor-p4'),
    path('add/p5/',views.add_vendor_p5,name='add-vendor-p5'),
]
