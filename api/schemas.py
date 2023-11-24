# Westeros/stark/schemas.py
from ninja import ModelSchema
from api.models import Usuario, Clase, Clase_Usuario


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


class ClaseIn(ModelSchema):
    class Config:
        model = Clase
        model_exclude = [
            "id",
        ]


class ClaseOut(ModelSchema):
    class Config:
        model = Clase
        model_fields = "__all__"


class Clase_UsuarioIn(ModelSchema):
    class Config:
        model = Clase_Usuario
        model_exclude = [
            "id",
        ]


class Clase_UsuarioOut(ModelSchema):
    class Config:
        model = Clase_Usuario
        model_fields = "__all__"
