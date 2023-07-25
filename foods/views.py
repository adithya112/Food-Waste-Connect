from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Food
from .forms import FoodModelForm
# CRUD-L

class HomePage(TemplateView):
    template_name = 'foods/home.html'

#List Operation
def food_list(request):
    foods = Food.objects.all()
    context = {
        'foods':foods
    }
    
    return render(request, 'foods/food_list.html', context)
    
    
class FoodListView(ListView):
    template_name = 'foods/food_list.html'
    context_object_name = 'foods'
    queryset = Food.objects.all()
    
    
#Retrive/Detail Operation

def food_detail(request, pk):
    food = Food.objects.get(id=pk)
    context = {
        'food':food
    }
    
    return render(request, 'foods/food_detail.html', context)


class FoodDetailView(DetailView):
    template_name = 'foods/food_detail.html'
    context_object_name = 'food'
    queryset = Food.objects.all()


#Create Operation
def food_create(request):
    form = FoodModelForm()
    if request.method=='POST':
        form = FoodModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foods:food-list')
    context = {
        'form':form
    }
    return render(request, 'foods/food_create.html', context)


class FoodCreateView(CreateView):
    template_name = 'foods/food_create.html'
    form_class = FoodModelForm
    
    def get_success_url(self):
        return reverse('foods:food-list')
    
    
#Update Operation
def food_update(request, pk):
    food = Food.objects.get(id=pk)
    form = FoodModelForm(instance=food)
    if request.method=='POST':
        form = FoodModelForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('foods:food-list')
    context = {
        'form':form
    }
    return render(request, 'foods/food_update.html', context)


class FoodUpdateView(UpdateView):
    template_name = 'foods/food_update.html'
    form_class = FoodModelForm
    queryset = Food.objects.all()
    
    def get_success_url(self):
        return reverse('foods:food-list')
    
    
#Delete Operation
def food_delete(request, pk):
    food = Food.objects.get(id=pk)
    food.delete()
    return redirect('foods:food-list')


class FoodDeleteView(DeleteView):
    template_name = 'foods/food_delete.html'
    queryset = Food.objects.all()
    
    def get_success_url(self):
        return reverse('foods:food-list')