from django.db import models
from datetime import datetime 

# Create your models here.

class Atividade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"
    
class Provincia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"
    
class Municipio(models.Model):
    nome = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete = models.PROTECT, verbose_name="Província")

    def __str__(self):
        return f"{self.nome}"
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete = models.PROTECT, verbose_name="Município")
    provincia = models.ForeignKey(Provincia, on_delete = models.PROTECT, verbose_name="Província")

    def __str__(self):
        return f"{self.nome} | {self.municipio} | {self.provincia}"
    
class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=14)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    titulo = models.CharField(max_length=50)
    contato1 = models.IntegerField(max_length=9)
    contato2 = models.IntegerField(max_length=9)
    endereco = models.ForeignKey(Bairro, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.documento} | {self.nome}"



class Turma(models.Model):
    nome = models.CharField(max_length=100)
    numero_aluno = models.IntegerField(max_length=30,verbose_name="Número de Alunos")
    horario = models.DateTimeField(verbose_name="Horário")
    duracao = models.DurationField(verbose_name="Duração")
    data_inicio = models.DateField()
    data_final = models.DateTimeField()
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.nome} | {self.atividade}"
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=14)
    data_matricula = models.DateField(default=datetime.now(), verbose_name="Data de Matrícula")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    altura = models.DecimalField(decimal_places=2, max_digits=3)
    peso = models.DecimalField(decimal_places=2, max_digits=5)
    contato1 = models.IntegerField(max_length=9)
    contato2 = models.IntegerField(max_length=9)
    endereco = models.ForeignKey(Bairro, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.documento} | {self.nome}"

class Equipa(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.turma} | {self.aluno}"