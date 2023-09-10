from django.db import models
from datetime import datetime 

# Create your models here.
horario_choices=[
    ("07:00:00","07:00:00"),
    ("16:00:00","16:00:00"),
    ("20:00:00","20:00:00"),
]

duracao_choices=[
    ("1H","1H"),
    ("2H","2H"),
    ("2H30","2H30")
]

class Atividade(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome}"
    
class Provincia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"
    
class Municipio(models.Model):
    nome = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete = models.PROTECT, verbose_name="Província")

    def __str__(self):
        return f"{self.nome}| {self.provincia}"
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete = models.PROTECT, verbose_name="Município")

    def __str__(self):
        return f"{self.nome} | {self.municipio}"
    
class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=14,unique=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    titulo = models.CharField(max_length=50)
    contato1 = models.DecimalField(max_digits=9, decimal_places=0,verbose_name="Contato Príncipal")
    contato2 = models.DecimalField(max_digits=9, decimal_places=0,verbose_name="Contato Alternatico")
    endereco = models.ForeignKey(Bairro, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.bi} | {self.nome}"



class Turma(models.Model):
    nome = models.CharField(max_length=100)
    numero_aluno = models.IntegerField(verbose_name="Número de Alunos")
    horario = models.CharField(max_length=20,verbose_name="Horário", choices=horario_choices)
    duracao = models.CharField(max_length=20,verbose_name="Duração", choices=duracao_choices)
    data_inicio = models.DateField()
    data_final = models.DateTimeField()
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.nome} | {self.atividade} | {self.horario}"
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=14, unique=True)
    data_matricula = models.DateField(default=datetime.now(), verbose_name="Data de Matrícula")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    altura = models.DecimalField(decimal_places=2, max_digits=3)
    peso = models.DecimalField(decimal_places=2, max_digits=5)
    contato1 = models.DecimalField(max_digits=9,decimal_places=0, verbose_name="Contato Príncipal")
    contato2 = models.DecimalField(max_digits=9,decimal_places=0, verbose_name="Contato Alternatico")
    endereco = models.ForeignKey(Bairro, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.bi} | {self.nome}"

class Equipa(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.turma} | {self.aluno}"