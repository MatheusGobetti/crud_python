from django.forms import ModelForm
from app.models import Residencias, Usuarios, Proprietarios

# Create the form class.
class ResidenciasForm(ModelForm):
  class Meta:
    model = Residencias
    fields = ['endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'preco_aluguel', 'preco_venda', 'cpf_proprietario']

class UsuariosForm(ModelForm):
  class Meta:
    model = Usuarios
    fields = ['nome', 'cpf', 'email', 'senha']

class ProprietariosForm(ModelForm):
  class Meta:
    model = Proprietarios
    fields = ['nome', 'cpf', 'email', 'telefone']