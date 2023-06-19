from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from aplicacion1.form import FormularioLogin, FormularioRegistro
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

class LandingPage(TemplateView):
    template_name = "aplicacion1/landing_page.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Usuarios(TemplateView):
    template_name = "aplicacion1/usuarios.html"

    def get(self, request, *args, **kwargs):
        titulo = "Lista de Usuarios"
        usuarios = User.objects.all()
        contexto = {
            "titulo": titulo,
            "usuarios": usuarios
        }
        return render(request, self.template_name, contexto)
    
class IngresoView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = FormularioLogin()
        return render(request, self.template_name, { "form": form })

    def post(self, request, *args, **kwargs):
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('catalogoProductos')
                else:
                    form.add_error('username', 'Credenciales incorrectas')
        return render(request, self.template_name, { "form": form })
        

class PaginaRestringidaView(TemplateView):
    template_name = 'aplicacion1/paginaRestringida.html'

    def get(self, request, *args, **kwargs):
        title = "Sitio Interno"
        productos = [
            {
                'imagen': "assets/img/producto1.png",
                'codigo': '019452',
                'nombre': 'Lavalozas Ecológico Fuzol',
                'precio': 1890
            },
            {
                'imagen': "assets/img/producto2.jpg",
                'codigo': '064532',
                'nombre': 'Antigrasas Mr. Músculo',
                'precio': 3550
            },
            {
                'imagen': "assets/img/producto3.jpg",
                'codigo': '033542',
                'nombre': 'Antigrasas Multiuso KH-7',
                'precio': 4290
            },
            {
                'imagen': "assets/img/producto4.jpg",
                'codigo': '075266',
                'nombre': 'Limpiador de piso Clorox',
                'precio': 2550
            },
            {
                'imagen': "assets/img/producto5.jpg",
                'codigo': '019452',
                'nombre': 'Limpiador de piso Igenix',
                'precio': 2590
            },
            {
                'imagen': "assets/img/producto6.png",
                'codigo': '022314',
                'nombre': 'Detergente líquido Ariel',
                'precio': 4500
            },
            {
                'imagen': "assets/img/producto7.jpg",
                'codigo': '085512',
                'nombre': 'Detergente en polvo Omo',
                'precio': 4200
            },
            {
                'imagen': "assets/img/producto8.jpg",
                'codigo': '005711',
                'nombre': 'Bolsa ecológica Superior',
                'precio': 460
            },
            ]

        primer_nombre = request.user.first_name or 'Usuari@ sin nombre registrado.'
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {'primer_nombre' : primer_nombre, 'segundo_nombre' : segundo_nombre, 'title' : title, 'productos': productos})
    
class RegistroView(TemplateView):
    template_name = 'registration/registro.html'

    def get(self, request, *args, **kwargs):
        form = FormularioRegistro()
        return render(request, self.template_name, {"formulario": form, "titulo": "Registro de Usuario"})

    def post(self, request, *args, **kwargs):
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if 'image' in request.FILES:
                image = request.FILES.get('image')
            else:
                image = form.ruta_fotoPerfil()
            # Crear una instancia de UserProfile y asociarla con el usuario
            profile = UserProfile(user=user, image=image)
            profile.save()

            # Asignar el perfil al usuario
            user.userprofile = profile
            user.save()
            mensajes = {"enviado": True, "resultado": "Has creado un nuevo usuario exitosamente"}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        return render(request, self.template_name, {"formulario": form, "mensajes": mensajes, "titulo": "Registro de Usuario"})
