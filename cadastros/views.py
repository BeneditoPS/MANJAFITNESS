from django.shortcuts import render
from .models import Atividade, Provincia, Municipio, Bairro, Instrutor, Turma, Aluno, Equipa
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.

#ATIVIDADE

class AtividadeCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['nome']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-atividade")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Atividade"
        return context


class AtividadeListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Atividade
    template_name="listarAtividade.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Atividade"
        return context

class AtividadeEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['nome']
    success_url = reverse_lazy("listar-atividade")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Atividade"
        return context

class AtividadeExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-atividade')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Atividade"
        return context
    
#PROVINCIA

class ProvinciaCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Provincia
    fields = ['nome']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-provincia")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Província"
        return context


class ProvinciaListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Provincia
    template_name="listarProvincia.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Província"
        return context

class ProvinciaEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Provincia
    fields = ['nome']
    success_url = reverse_lazy("listar-provincia")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Provincia"
        return context

class ProvinciaExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Provincia
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-provincia')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Provincía"
        return context

#MUNICIPIO

class MunicipioCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Municipio
    fields = ['nome', 'provincia']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-municipio")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Municipio"
        return context


class MunicipioListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Municipio
    template_name="listarMunicipio.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Municipio"
        return context

class MunicipioEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Municipio
    fields = ['nome','provicia']
    success_url = reverse_lazy("listar-municipio")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Municipio"
        return context

class MunicipioExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Municipio
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-municipio')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Municipio"
        return context
    
#BAIRRO
class BairroCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Bairro
    fields = ['nome','municipio','provincia']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-bairro")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Bairro"
        return context


class BairroListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Bairro
    template_name="listarBairro.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Bairro"
        return context

class BairroEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Bairro
    fields = ['nome','municipio','provincia']
    success_url = reverse_lazy("listar-bairro")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Bairro"
        return context

class BairroExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Bairro
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-bairro')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Bairro"
        return context
    
#INSTRUTOR
class InstrutorCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Instrutor
    fields = ['nome', 'documento', 'data_nascimento', 'titulo', 'contato1', 'contato2', 'endereco']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-instrutor")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Instrutor"
        return context


class InstrutorListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Instrutor
    template_name="listarInstrutor.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Instrutor"
        return context

class InstrutorEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Bairro
    fields = ['nome', 'documento', 'data_nascimento', 'titulo', 'contato1', 'contato2', 'endereco']
    success_url = reverse_lazy("listar-instrutor")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Instrutor"
        return context

class InstrutorExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Instrutor
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-instrutor')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Instrutor"
        return context
    

#TURMA
class TurmaCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Turma
    fields = ['nome', 'numero_aluno', 'horario', 'duracao', 'data_inicio', 'data_final', 'instrutor', 'atividade']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-turma")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Turma"
        return context


class TurmaListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Turma
    template_name="listarTurma.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Turma"
        return context

class TurmaEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Turma
    fields = ['nome', 'numero_aluno', 'horario', 'duracao', 'data_inicio', 'data_final', 'instrutor', 'atividade']
    success_url = reverse_lazy("listar-turma")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Turma"
        return context

class TurmaExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Turma
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-turma')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Turma"
        return context
    
#ALUNO
class AlunoCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Aluno
    fields = ['nome', 'documento', 'data_nascimento', 'altura', 'peso', 'contato1', 'contato2', 'endereco']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-aluno")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Aluno"
        return context


class AlunoListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Aluno
    template_name="listarAluno.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Aluno"
        return context

class AlunoEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Aluno
    fields = ['nome', 'documento', 'data_nascimento', 'altura', 'peso', 'contato1', 'contato2', 'endereco']
    success_url = reverse_lazy("listar-aluno")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Aluno"
        return context

class AlunoExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-aluno')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Aluno"
        return context
    
#EQUIPA
class EquipaCadastrar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Equipa
    fields = ['turma','aluno']
    template_name="cadastrar.html"
    success_url = reverse_lazy("listar-equipa")
    group_required = u"admin"
    login_url = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastar Equipa"
        return context


class EquipaListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Equipa
    template_name="listarEquipa.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Equipa"
        return context

class EquipaEditar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Equipa
    fields = ['turma','aluno']
    success_url = reverse_lazy("listar-equipa")
    template_name = "cadastrar.html"
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Equipa"
        return context

class EquipaExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Equipa
    template_name = "excluir.html"
    success_url = reverse_lazy('listar-equipa')
    group_required = u"admin"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Equipa"
        return context