from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    path("", include("social_django.urls", namespace="social")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
