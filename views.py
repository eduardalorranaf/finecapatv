from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservaForm
from .models import Reserva


def index(request):
    total_reservas = Reserva.objects.count()
    return render(request, "reservas/index.html", {'total_reservas' : total_reservas})


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('reserva_listar')
    else:
        form = ReservaForm()

    return render(request, "reservas/reservaForm.html", {'form': form})


def reserva_listar(request):
    reservas = Reserva.objects.all()
    return render(request, "reservas/reservas.html", {'reservas': reservas})


def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)
        
    return render(request, 'reservas/reservaForm.html', {'form': form})


def reserva_deletar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')
