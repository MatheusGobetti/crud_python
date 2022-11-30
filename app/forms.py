from django.forms import ModelForm
from app.models import Residencias

# Create the form class.
class ResidenciasForm(ModelForm):
  class Meta:
    model = Residencias
    fields = ['endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'preco_aluguel', 'preco_venda', 'cpf_proprietario']