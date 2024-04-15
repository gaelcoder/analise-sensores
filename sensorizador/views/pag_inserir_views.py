from sensorizador.models import Sensor
from django.core.paginator import Paginator
from django.http import Http404
from django.utils import timezone
from datetime import timedelta, datetime
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    sensores = Sensor.objects.all()\
        .order_by('-timestamp')
    
    paginator = Paginator(sensores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        'sensorizador/index.html',
        context,
    )

def search(request):

    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('sensorizador:index')

    sensores = Sensor.objects\
        .filter(equipmentID__icontains=search_value)\
        .order_by('-timestamp')

    paginator = Paginator(sensores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contex = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    return render(
        request,
        'sensorizador/index.html',
        contex,
    )


def pesquisa(request, id):
    sensor_escolhido = get_object_or_404(Sensor.objects, pk=id)
    
    contex = {
        'sensores': sensor_escolhido,
    }
    return render(
        request,
        'sensorizador/pesquisa.html',
        contex,
    )

def analise(request):

    queryset = Sensor.objects.all()
    horario_atual = timezone.now()
    search_valuep = request.GET.get('p', '').strip()

    def verificador(diferenca_cont):
        soma = 0
        cont = 0
        difatual = diferenca_cont
        for sensor in queryset:
            if (sensor.equipmentID.upper() == search_valuep) | (sensor.equipmentID.lower() == search_valuep) :
                if sensor.timestamp >= difatual: 
                    soma += float(sensor.value)
                    cont += 1
                    difatual = difatual + timedelta(hours=+1)
        if (cont > 0):
            media = soma / cont
        else:
            media=0
        return media
    
    def difdia(datahj):
        horaatual = datahj
        contdiaum = horaatual - timedelta(hours=24)
        media = verificador(contdiaum)
        return media
    
    def difdoisdias(datahj):
        horaatual = datahj
        contdiadois = horaatual - timedelta(hours=48)
        media = verificador(contdiadois)
        return media
    
    def difsemana(datahj):
        horaatual = datahj
        contsemana = horaatual - timedelta(days=7)
        media = verificador(contsemana)
        return media
    
    def difmes(datahj):
        horaatual = datahj
        contmes = horaatual - timedelta(days=30)
        media = verificador(contmes)
        return media

    mediadia = difdia(horario_atual)
    mediadois = difdoisdias(horario_atual)
    mediasemana = difsemana(horario_atual)
    mediames = difmes(horario_atual)
    print(mediadia, mediames, mediasemana, mediadois)

    labels = ['24h', '48h', '1 Sem.', '1 Mês']
    data = [mediadia, mediadois, mediasemana, mediames]


    context = {
        'search_valuep': search_valuep,
        'labels': labels,
        'data': data,
    }

    return render(
        request,
        'sensorizador/analise.html',
        context,
    )