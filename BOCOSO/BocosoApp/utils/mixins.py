from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse

class ABMMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.rol.id == 1 or request.user.rol.id == 2:
            return super().dispatch(request,*args,**kwargs)
        return redirect('index')


class AutoridadMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol.id == 1:
            return super().dispatch(request,*args,**kwargs)
        return redirect('index')
    

class PersonalMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol.id == 2:
            return super().dispatch(request,*args,**kwargs)
        return redirect('index')
    
def ABM():
    def permisos_requeridos(f):
        def check(request,*args,**kwargs):
            if request.user.rol:
                if not request.user.rol.id == 1 and not request.user.rol.id == 2:
                    raise PermissionDenied
                return f(request,*args,**kwargs)
            raise PermissionDenied
        return check
    return permisos_requeridos

def is_personal_required():
    def permisos_requeridos(f):
        def check(request,*args,**kwargs):
            if request.user.rol:
                if not request.user.rol.id == 2:
                    raise PermissionDenied
                return f(request,*args,**kwargs)
            raise PermissionDenied
        return check
    return permisos_requeridos

def es_el_usuario():
    def permisos_requeridos(f):
        def check(request,*args,**kwargs):
            if not request.user.id == kwargs.get('pk'):
                raise PermissionDenied
            return f(request,*args,**kwargs)
        return check
    return permisos_requeridos