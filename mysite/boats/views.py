from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from boats.models import Boat, Type
#from cats.forms import MakeForm

# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Type.objects.all().count()
        cl = Boat.objects.all()

        ctx = {'type_count': bc, 'boat_list': cl}
        return render(request, 'boats/boat_list.html', ctx)


class TypeView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Type.objects.all()
        ctx = {'type_list': bl}
        return render(request, 'boats/type_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class TypeCreate(LoginRequiredMixin, CreateView):
    fields ='__all__'
    model = Type
    success_url = reverse_lazy('boats:all')


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields ='__all__'
    success_url = reverse_lazy('boats:all')
    template = 'boats/type_form.html'


class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields ='__all__'
    success_url = reverse_lazy('boats:all')
    template = 'boats/type_confirm_delete.html'


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class BoatCreate(LoginRequiredMixin, CreateView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class BoatUpdate(LoginRequiredMixin, UpdateView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')


class BoatDelete(LoginRequiredMixin, DeleteView):
    model = Boat
    fields = '__all__'
    success_url = reverse_lazy('boats:all')