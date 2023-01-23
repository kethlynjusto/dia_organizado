from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy

class UsuarioCreate(CreateView):
    template_name = 'usuario/form_cadastro_usuario.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario/form_login.html')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registrar Novo Usuário'
        context['botao'] = 'Cadastrar'

        return context
