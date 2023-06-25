from django.contrib import admin
from .models import Atividade, Provincia, Municipio, Bairro, Instrutor, Turma, Aluno, Equipa

# Register your models here.
admin.site.register(Atividade)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Bairro)
admin.site.register(Instrutor)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Equipa)