from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch
from .forms import FeedingForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finch/index.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finch/detail.html', {
      'finch': finch, 'feeding_form': feeding_form
    })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['color', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finch'

def add_feeding(request, cat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)
