from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Colaborador
from .forms import ColaboradorForm


@login_required
def lista_colaboradores(request):
    colaboradores = Colaborador.objects.order_by('nome')
    return render(request, 'colaboradores/list.html', {'colaboradores': colaboradores})


@login_required
def novo_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso.')
            return redirect('colaboradores:lista')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/form.html', {'form': form, 'title': 'Novo Colaborador'})


@login_required
def editar_colaborador(request, pk):
    obj = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado.')
            return redirect('colaboradores:lista')
    else:
        form = ColaboradorForm(instance=obj)
    return render(request, 'colaboradores/form.html', {'form': form, 'title': 'Editar Colaborador'})


@permission_required('colaboradores.delete_colaborador', raise_exception=True)
def excluir_colaborador(request, pk):
    obj = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Colaborador excluído.')
        return redirect('colaboradores:lista')
    return render(request, 'colaboradores/confirm_delete.html', {'object': obj})
