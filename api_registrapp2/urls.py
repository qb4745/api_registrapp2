from django.contrib import admin
from django.urls import path


from ninja import NinjaAPI

from api.api import router as usuario_router
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
]

api = NinjaAPI()
api.add_router("/usuario/", usuario_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", RedirectView.as_view(url="/api/docs"), name="redirect-to-docs"),
]
