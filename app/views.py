from django.shortcuts import render, redirect
from app.forms import ResidenciasForm, UsuariosForm, ProprietariosForm
from app.models import Residencias, Usuarios, Proprietarios
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
import urllib

# Create your views here.
def home(request):
  data = {}
  search = request.GET.get('search')
  if search:
    data['db'] = Residencias.objects.filter(endereco__icontains=search)
  else:
    data['db'] = Residencias.objects.all()

  return render(request, 'index.html', data)

def json(request):
  data = list(Residencias.objects.values())
  return JsonResponse(data, safe=False)

def json_txt(request):
  response = HttpResponse(content_type='text/plain')
  response['Content-Disposition'] = 'attachment; filename=json_data.txt'
  lines = list(Residencias.objects.values())
  response.writelines(lines)
  return response

def sobre(request):
  return render(request, 'sobre.html')

# Residencias operations:
def form(request):
  data = {}
  data['form'] = ResidenciasForm()
  return render(request, 'form.html', data)

def create(request):
  form = ResidenciasForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('home')

def view(request, pk):
  data = {}
  data['db'] = Residencias.objects.get(pk=pk)
  return render(request, 'view.html', data)

def edit(request, pk):
  data = {}
  data['db'] = Residencias.objects.get(pk=pk)
  data['form'] = ResidenciasForm(instance=data['db'])
  return render(request, 'form.html', data)

def update(request, pk):
  data = {}
  data['db'] = Residencias.objects.get(pk=pk)
  form = ResidenciasForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return redirect('home')

def delete(request, pk):
  db = Residencias.objects.get(pk=pk)
  db.delete()
  return redirect('home')

#Usuarios operations:
def login(request):
  data = {}
  data['login_form'] = UsuariosForm()
  return render(request, 'login.html', data)

def validar_login(request, pk):
  data = {}
  data['db'] = Usuarios.objects.get(pk=pk)
  return render(request, 'view.html', data)

def cadastro_form(request):
  data = {}
  data['cadastro_form'] = UsuariosForm()
  return render(request, 'cadastro.html', data)

def create_cadastro(request):
  form = UsuariosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('login')

def update_cadastro(request, pk):
  data = {}
  data['db'] = Usuarios.objects.get(pk=pk)
  form = UsuariosForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return redirect('login')


#Proprietarios operations:
def index_proprietarios(request):
  data = {}
  data['db_p'] = Proprietarios.objects.all()
  return render(request, 'index_proprietarios.html', data)

def form_proprietarios(request):
  data = {}
  data['form_proprietarios'] = ProprietariosForm()
  return render(request, 'form_proprietarios.html', data)

def create_proprietarios(request):
  form = ProprietariosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('index_proprietarios')

def view_proprietarios(request, pk):
  data = {}
  data['db_p'] = Proprietarios.objects.get(pk=pk)
  return render(request, 'view_proprietarios.html', data)

def edit_proprietarios(request, pk):
  data = {}
  data['db_p'] = Proprietarios.objects.get(pk=pk)
  data['form_proprietarios'] = ProprietariosForm(instance=data['db_p'])
  return render(request, 'form_proprietarios.html', data)

def update_proprietarios(request, pk):
  data = {}
  data['db_p'] = Proprietarios.objects.get(pk=pk)
  form = ProprietariosForm(request.POST or None, instance=data['db_p'])
  if form.is_valid():
    form.save()
    return redirect('form_proprietarios')

def delete_proprietarios(request, pk):
  db = Proprietarios.objects.get(pk=pk)
  db.delete()
  return redirect('form_proprietarios')

#Import Data Operations:
def import_residencia(data):
  url = "https://raw.githubusercontent.com/MatheusGobetti/crud_python/main/db.json"
  response = urllib.request.urlopen(url)
  dados = response.read()
  print('LENGTH: %d' %len(dados))
  print(dados)

  #Func = open("app/templates/json_imported.html","w")
  #Func.write(str(response.read()))
  #Func.close()

  return redirect('json_imported')

def json_imported(request):
  data = {}
  return render(request, 'json_imported.html', data)