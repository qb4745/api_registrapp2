# Westeros/stark/schemas.py
from ninja import ModelSchema
from api.models import Usuario


class UsuarioIn(ModelSchema):
    class Config:
        model = Usuario
        model_exclude = [
            "id",
        ]


class UsuarioOut(ModelSchema):
    class Config:
        model = Usuario
        model_fields = "__all__"
