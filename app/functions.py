
import requests
from app.models import Residencias 
from django.core.management.base import BaseCommand
 
IMPORT_URL = 'https://jsonplaceholder.typicode.com/photos' 
 
class Command(BaseCommand):
  def import_residencia(self, data):
    endereco = data.get('endereco', None)
    numero = data.get('numero', None)
    complemento = data.get('complemento', None)
    bairro = data.get('bairro', None)
    cidade = data.get('cidade', None)
    estado = data.get('estado', None)
    preco_aluguel = data.get('preco_aluguel', None)
    preco_venda = data.get('preco_venda', None)
    cpf_proprietario = data.get('cpf_proprietario', None)

    residencia, created = Residencias.objects.get_or_create(
      endereco=endereco,
      numero=numero,
      complemento=complemento,
      bairro=bairro,
      cidade=cidade,
      estado=estado,
      preco_aluguel=preco_aluguel,
      preco_venda=preco_venda,
      cpf_proprietario=cpf_proprietario,
    )
    if created:
      residencia.save()
      display_format = "\Residencia, {}, foi salva."
      print(display_format.format(residencia))

      def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
          url=IMPORT_URL,
          headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        for data_object in data:
          self.import_residencia(data_object)