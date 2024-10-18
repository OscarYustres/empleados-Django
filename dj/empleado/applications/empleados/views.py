from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# models
from .models import Empleado

# Create your views here.

class InicioView(TemplateView):
    """ pagina de inicio """
    template_name = 'inicio.html'
    #queryset = Empleado.objects.filter(
    #     departamento__shor_name='Otro'
    # )



class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    context_object_name = 'empleados'
    # ya no necesito el modelo por que lo vamos a filtrar model = Empleado
    
    def get_queryset(self):
        
        palabra_clave = self.request.GET.get("kword", '')
        print('===========',palabra_clave)
        lista=Empleado.objects.filter(
            # first_name=palabra_clave
            first_name__icontains=palabra_clave
        )
        
        return lista
    
    
class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    #queryset = Empleado.objects.filter(
    #     departamento__shor_name='Otro'
    # )
    
    
    def get_queryset(self):
        area=self.kwargs['shorname']
        #el codigo que se necesite
        lista=Empleado.objects.filter(
        departamento__shor_name=area
        )
        return lista
    
class ListEmpleadosByKword(ListView):
    """ lista empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('*********************')
        palabra_clave = self.request.GET.get("kword", '')
        print('===========',palabra_clave)
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('lista resultado:', lista)
        return lista


class ListHabilidadesEmpleado(ListView):
        template_name = 'persona/habilidades.html'
        context_object_name = 'habilidades'
        
        def get_queryset(self):
            empleado = Empleado.objects.get(id=7)
            #print(empleado.habilidades.all())
            return empleado.habilidades.all()
        

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        ]
    #fields = ('__all__')
    #una forma de hacer redireccionamiento
    #success_url = '/success'
    success_url = reverse_lazy('persona_app:correcto')
    
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        ]
    success_url = reverse_lazy('persona_app:correcto')
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METHOD POST*************')
        print('===============')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        #logica del proceso
        print('***************METHOD form valid*************')
        print('***************')
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name='persona/delete.html'
    success_url = reverse_lazy('persona_app:correcto')    