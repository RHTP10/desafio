from django.shortcuts import render, redirect

# Create your views here.
from dono.forms import DonoForm
from dono.models import Dono


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
    return render(request, 'cadastro.html', args)
def delete(request, id):
    dono = Dono.objects.get(id=id)

    args = {
        'dono': dono
    }
 
    dono.delete()
    return render(request, 'delete.html', args)

def update(request, id):
    dono = Dono.objects.get(id=id)
    form = DonoForm(request.POST or None, instance=dono)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{dono.id}')

    args = {
        'dono':dono,
        'form':form
    }
    return render(request, 'update.html', args)