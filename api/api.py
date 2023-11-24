from django.shortcuts import get_object_or_404
from ninja import Router
from api.schemas import UsuarioIn, UsuarioOut
from api.models import Usuario

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
