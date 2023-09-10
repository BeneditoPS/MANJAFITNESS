from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
import plotly.offline 
import plotly.express as plt
from cadastros.models import Turma
# Create your views here.

class IndexViews(TemplateView):
    template_name="index.html"

class SuplementoViews(TemplateView):
    template_name="suplemento.html"

class EstatisticaViews(TemplateView):
    template_name="estatistica.html"

def grafico(request):
    aluno=Turma.objects.all()

    fig = plt.line(
        x=[c.nome for c in aluno],
        y=[c.numero_aluno for c in aluno],
    )

    chart=fig.to_html()

    context = {'chart': chart}
    return render(request, 'estatistica.html', context)