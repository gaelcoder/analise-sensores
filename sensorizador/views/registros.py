from django.shortcuts import render, redirect
from sensorizador.forms import SensorForm
from pathlib import Path
import json

CAMINHO_ATUALMENTE = Path(__file__).parent / 'dadosrapidos.json'

def create(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            form.save()
            with open(CAMINHO_ATUALMENTE, 'w') as arquivo:
                json.dump(request.POST, arquivo, ensure_ascii=False, indent=2)
            arquivo.close()
            return redirect('sensorizador:registrar')
        

        return render(
            request,
            'sensorizador/create.html',
            context,
        )
    
    context = {
            'form': SensorForm(),
        }
    
    return render(
        request,
        'sensorizador/create.html',
        context,
    )


