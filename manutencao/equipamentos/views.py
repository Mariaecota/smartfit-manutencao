from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm  # Vamos criar esse form logo abaixo!



def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)

    if request.method == "POST":
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamentos')  # Redireciona de volta para a lista
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, 'equipamentos/editar.html', {'form': form, 'equipamento': equipamento})

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/lista.html', {'equipamentos': equipamentos})
