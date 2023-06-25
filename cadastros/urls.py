from django.urls import path
from .views import AtividadeCadastrar, AtividadeListar, AtividadeEditar, AtividadeExcluir
from .views import ProvinciaCadastrar, ProvinciaListar, ProvinciaEditar, ProvinciaExcluir
from .views import MunicipioCadastrar, MunicipioListar, MunicipioEditar, MunicipioExcluir
from .views import BairroCadastrar, BairroListar, BairroEditar, BairroExcluir
from .views import InstrutorCadastrar, InstrutorListar, InstrutorEditar, InstrutorExcluir
from .views import TurmaCadastrar, TurmaListar, TurmaEditar, TurmaExcluir
from .views import AlunoCadastrar, AlunoListar, AlunoEditar, AlunoExcluir
from .views import EquipaCadastrar, EquipaListar, EquipaEditar, EquipaExcluir

urlpatterns=[
    #ATIVIDADE
    path("cadastrar/atividade", AtividadeCadastrar.as_view(), name="cadastrar-atividade"),

    path("listar/atividade", AtividadeListar.as_view(), name="listar-atividade"),

    path("editar/atividade/<int:pk>", AtividadeEditar.as_view(), name="editar-atividade"),

    path("excluir/atividade/<int:pk>", AtividadeExcluir.as_view(), name="excluir-atividade"),

     #PROVINCIA
    path("cadastrar/provincia", ProvinciaCadastrar.as_view(), name="cadastrar-provincia"),

    path("listar/provincia", ProvinciaListar.as_view(), name="listar-provincia"),

    path("editar/provincia/<int:pk>", ProvinciaEditar.as_view(), name="editar-provincia"),

    path("excluir/provincia/<int:pk>", ProvinciaExcluir.as_view(), name="excluir-provincia"),

     #MUNICIPIO
    path("cadastrar/municipio", MunicipioCadastrar.as_view(), name="cadastrar-municipio"),

    path("listar/municipio", MunicipioListar.as_view(), name="listar-municipio"),

    path("editar/municipio/<int:pk>", MunicipioEditar.as_view(), name="editar-municipio"),

    path("excluir/municipio/<int:pk>", MunicipioExcluir.as_view(), name="excluir-municipio"),

     #BAIRRO
    path("cadastrar/bairro", BairroCadastrar.as_view(), name="cadastrar-bairro"),

    path("listar/bairro", BairroListar.as_view(), name="listar-bairro"),

    path("editar/bairro/<int:pk>", BairroEditar.as_view(), name="editar-bairro"),

    path("excluir/bairro/<int:pk>", BairroExcluir.as_view(), name="excluir-bairro"),

       #INSTRUTOR
    path("cadastrar/instrutor", InstrutorCadastrar.as_view(), name="cadastrar-instrutor"),

    path("listar/instrutor", InstrutorListar.as_view(), name="listar-instrutor"),

    path("editar/instrutor/<int:pk>", InstrutorEditar.as_view(), name="editar-instrutor"),

    path("excluir/instrutor/<int:pk>", InstrutorExcluir.as_view(), name="excluir-instrutor"),

       #TURMA
    path("cadastrar/turma", TurmaCadastrar.as_view(), name="cadastrar-turma"),

    path("listar/turma", TurmaListar.as_view(), name="listar-turma"),

    path("editar/turma/<int:pk>", TurmaEditar.as_view(), name="editar-turma"),

    path("excluir/turma/<int:pk>", TurmaExcluir.as_view(), name="excluir-turma"),

       #ALUNO
    path("cadastrar/aluno", AlunoCadastrar.as_view(), name="cadastrar-aluno"),

    path("listar/aluno", AlunoListar.as_view(), name="listar-aluno"),

    path("editar/aluno/<int:pk>", AlunoEditar.as_view(), name="editar-aluno"),

    path("excluir/aluno/<int:pk>", AlunoExcluir.as_view(), name="excluir-aluno"),

       #EQUIPA
    path("cadastrar/equipa", EquipaCadastrar.as_view(), name="cadastrar-equipa"),

    path("listar/equipa", EquipaListar.as_view(), name="listar-equipa"),

    path("editar/equipa/<int:pk>", EquipaEditar.as_view(), name="editar-equipa"),

    path("excluir/equipa/<int:pk>", EquipaExcluir.as_view(), name="excluir-equipa"),

]