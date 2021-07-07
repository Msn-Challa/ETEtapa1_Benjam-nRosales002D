from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name="index"),
    path('tienda/',views.tienda, name="tienda"),
    path('proveedor/',views.proveedor, name="proveedor"),
    path('form_proveedor/',views.form_proveedor, name="form_proveedor"),
    path('ver/',views.ver, name="ver"),
    path('form_modproveedor/<id>', views.form_modproveedor, name="form_modproveedor"),
    path('form_delproveedor/<id>', views.form_delproveedor, name="form_delproveedor")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)