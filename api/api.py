from django.shortcuts import get_object_or_404
from ninja import Router
from api.schemas import (
    UsuarioIn,
    UsuarioOut,
    ClaseIn,
    ClaseOut,
    Clase_UsuarioIn,
    Clase_UsuarioOut,
)
from api.models import Usuario, Clase, Clase_Usuario

router = Router()


@router.post("/crear", response=UsuarioOut, url_name="create_usuario")
def create_usuario(request, payload: UsuarioIn):
    usuario = Usuario.objects.create(**payload.dict())
    return usuario


@router.get("/lista", response=list[UsuarioOut], url_name="list_usuarios")
def list_usuarios(request):
    return Usuario.objects.all()


@router.get("/lista/{int:usuario_id}", response=UsuarioOut, url_name="usuario")
def get_usuario(request, usuario_id):
    return get_object_or_404(Usuario, id=usuario_id)


@router.put("/modifica/{int:usuario_id}", response=UsuarioOut)
def update_usuario(request, usuario_id, payload: UsuarioIn):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    for name, value in payload.dict().items():
        setattr(usuario, name, value)

    usuario.save()
    return usuario


@router.delete("/elimina/{int:usuario_id}")
def update_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()

    return {"success": True}


@router.post("/crear_clase", response=ClaseOut, url_name="create_clase")
def create_clase(request, payload: ClaseIn):
    clase = Clase.objects.create(**payload.dict())
    return clase


@router.get("/lista_clase", response=list[ClaseOut], url_name="list_clases")
def list_clases(request):
    return Clase.objects.all()


@router.get("/lista_clase/{int:clase_id}", response=ClaseOut, url_name="clase")
def get_clase(request, clase_id):
    return get_object_or_404(Clase, id=clase_id)


@router.put("/modifica_clase/{int:clase_id}", response=ClaseOut)
def update_clase(request, clase_id, payload: ClaseIn):
    clase = get_object_or_404(Clase, id=clase_id)

    for name, value in payload.dict().items():
        setattr(clase, name, value)

    clase.save()
    return clase


@router.delete("/elimina_clase/{int:clase_id}")
def update_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    clase.delete()

    return {"success": True}


@router.post(
    "/crear_clase_usuario", response=Clase_UsuarioOut, url_name="create_clase_usuario"
)
def create_clase_usuario(request, payload: Clase_UsuarioIn):
    clase_usuario = Clase_Usuario.objects.create(**payload.dict())
    return clase_usuario


@router.get(
    "/lista_clase_usuario",
    response=list[Clase_UsuarioOut],
    url_name="list_clases_usuarios",
)
def list_clases_usuarios(request):
    return Clase_Usuario.objects.all()


@router.get(
    "/lista_clase_usuario/{int:clase_usuario_id}",
    response=Clase_UsuarioOut,
    url_name="clase_usuario",
)
def get_clase_usuario(request, clase_usuario_id):
    return get_object_or_404(Clase_Usuario, id=clase_usuario_id)


@router.put("/modifica_clase_usuario/{int:clase_usuario_id}", response=Clase_UsuarioOut)
def update_clase_usuario(request, clase_usuario_id, payload: Clase_UsuarioIn):
    clase_usuario = get_object_or_404(Clase_Usuario, id=clase_usuario_id)

    for name, value in payload.dict().items():
        setattr(clase_usuario, name, value)

    clase_usuario.save()
    return clase_usuario


@router.delete("/elimina_clase_usuario/{int:clase_usuario_id}")
def delete_clase_usuario(request, clase_usuario_id):
    clase_usuario = get_object_or_404(Clase_Usuario, id=clase_usuario_id)
    clase_usuario.delete()

    return {"success": True}
