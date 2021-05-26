from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Coche, Camioneta, Bicicleta, Motocicleta
from .forms import CocheForm, CamionetaForm, BicicletaForm, MotocicletaForm
from django.http import HttpResponseRedirect


class VehicleList(ListView):
    model = Coche

class CreateCoche(CreateView):
    model = Coche
    form_class = CocheForm
    success_url = '/?ok'

class CreateCamioneta(CreateView):
    model = Camioneta
    form_class = CamionetaForm
    success_url = '/?ok'

class CreateBicicleta(CreateView):
    model = Bicicleta
    form_class = BicicletaForm
    success_url = '/?ok'

class CreateMotocicleta(CreateView):
    model = Motocicleta
    form_class = MotocicletaForm
    success_url = '/?ok'

# Update views

class UpdateCoche(UpdateView):
    model = Coche
    form_class = CocheForm
    success_url = '/?up'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

class UpdateCamioneta(UpdateView):
    model = Camioneta
    form_class = CamionetaForm
    success_url = '/?up'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

class UpdateBicicleta(UpdateView):
    model = Bicicleta
    form_class = BicicletaForm
    success_url = '/?up'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

class UpdateMotocicleta(UpdateView):
    model = Motocicleta
    form_class = MotocicletaForm
    success_url = '/?up'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

# Delete views

class DeleteCoche(DeleteView):
    model = Coche
    success_url = '/?del'

class DeleteCamioneta(DeleteView):
    model = Camioneta
    success_url = '/?del'

class DeleteBicicleta(DeleteView):
    model = Bicicleta
    success_url = '/?del'

class DeleteMotocicleta(DeleteView):
    model = Motocicleta
    success_url = '/?del'

class ListVehicle(ListView):

    template_name = 'vehicle/list-vehicle.html'
    def get_queryset(self):
        Coches = Coche.objects.all()
        Camionetas = Camioneta.objects.all()
        Bicicletas = Bicicleta.objects.all()
        Motocicletas = Motocicleta.objects.all()
        queryset = []
        for c in Coches:
            queryset.append(c)
        for g in Camionetas:
            queryset.append(g)
        for b in Bicicletas:
            queryset.append(b)
        for m in Motocicletas:
            queryset.append(m)
        return queryset