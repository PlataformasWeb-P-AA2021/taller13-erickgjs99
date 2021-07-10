from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
    Departamento


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Nombre del edificio'),
            'direccion': _('Dirección del edificio '),
            'ciudad': _('Ciudad del edificio '),
            'tipo': _('De que tipo es el edificio'),
        }





class DepartamentoForm(ModelForm):
    class Meta:
        fields = ['nombreProp', 'costo', 'numCuartos', 'edificio']
        labels = {
            'nombreProp': _('Nombre del propietario del departamento'),
            'costo': _('Costo del departamento '),
            'numCuartos': _('Cuántos cuartos tiene el departamento'),
            'edificio': _('A que edificio pertenece el departamento'),
        }
    
    


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
  

    class Meta:
        model = Departamento
        fields = ['nombreProp', 'costo', 'numCuartos', 'edificio']
    
    


