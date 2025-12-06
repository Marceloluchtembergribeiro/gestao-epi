# ...existing code...
from django.shortcuts import render, redirect, get_object_or_404
# from .models import Colaborador, EPI   # removido (import localizado dentro das funções)
# from .forms import ColaboradorForm, EPIForm  # removido (import localizado dentro das funções)
# ...existing code...


def colaborador_lista(request):
    from .models import Colaborador
    colaboradores = Colaborador.objects.all()
    return render(request, 'epis/colaborador_lista.html', {'colaboradores': colaboradores})


def colaborador_novo(request):
    from .forms import ColaboradorForm
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaborador_lista')
    else:
        form = ColaboradorForm()
    return render(request, 'epis/colaborador_form.html', {'form': form})


def colaborador_editar(request, id):
    from .models import Colaborador
    from .forms import ColaboradorForm
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador_lista')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'epis/colaborador_form.html', {'form': form})


def colaborador_excluir(request, id):
    from .models import Colaborador
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    return redirect('colaborador_lista')


def epi_lista(request):
    from .models import EPI
    epis = EPI.objects.all()
    return render(request, 'epis/epi_lista.html', {'epis': epis})


def epi_novo(request):
    from .forms import EPIForm
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('epi_lista')
    else:
        form = EPIForm()
    return render(request, 'epis/epi_form.html', {'form': form})


def epi_editar(request, id):
    from .models import EPI
    from .forms import EPIForm
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        form = EPIForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            return redirect('epi_lista')
    else:
        form = EPIForm(instance=epi)
    return render(request, 'epis/epi_form.html', {'form': form})


def epi_excluir(request, id):
    from .models import EPI
    epi = get_object_or_404(EPI, id=id)
    epi.delete()
    return redirect('epi_lista')
# ...existing code...
