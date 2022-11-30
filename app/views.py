from shutil import make_archive
from wsgiref.types import FileWrapper
from django.shortcuts import render, redirect
from app.forms import ResidenciasForm
from app.models import Residencias
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
import zipfile

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

