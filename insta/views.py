from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Country, City
from .forms import CountryForm



class CountryView(CreateView):
    model = Country
    form = CountryForm
    template_name = 'insta/country.html'
    context_object_name = 'countries'

    def get(self, request):
        form = CountryForm()
        countries = Country.objects.all()
        return render(request, self.template_name, {'form': form, 'countries': countries})
    
    def post(self, request):
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # city = requset(url, data = {'name': request.POST.get('name')})
            # City.objects.create(name=city['name'], country=Country.objects.get(pk=city['country']))
                           
            return redirect('country')
        return render(request, self.template_name, {'form': form})

class CoutryUpdate(UpdateView):
    model = Country
    form = CountryForm
    template_name = 'insta/country.html'


    def get(self, request, pk):
        country = Country.objects.get(pk=pk)
        form = CountryForm(instance=country)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, pk):
        country = Country.objects.get(pk=pk)
        form = CountryForm(request.POST, request.FILES, instance=country)
        print(request.POST.get('name'))
        if form.is_valid():
            form.save()
            return redirect('country')
        return render(request, self.template_name, {'form': form})

class CityView(DetailView):
    model = City
    template_name = 'insta/city.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.get
        return context

class HomeView(View):
    def get(self, request):
        return HttpResponse('Hello World with class!')

def home(request):
    return HttpResponse('Hello World!')

def redirectview(request):
    return redirect('home-name')

def redirecthomeclass(request):
    return redirect('home-class')
