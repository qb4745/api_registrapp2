from django.contrib import admin
from django.urls import path


from ninja import NinjaAPI

from api.api import router as router
from api.api import router as clase_router
from api.api import router as clase_usuario_router
from django.views.generic import RedirectView


api = NinjaAPI()
api.add_router("/registrapp/", router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", RedirectView.as_view(url="/api/docs"), name="redirect-to-docs"),
]
