# Generated by Django 4.2.2 on 2023-06-26 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_aluno_instrutor_turma_equipa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bairro',
            name='provincia',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='contato1',
            field=models.IntegerField(verbose_name='Contato Príncipal'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='contato2',
            field=models.IntegerField(verbose_name='Contato Alternatico'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_matricula',
            field=models.DateField(default=datetime.datetime(2023, 6, 26, 1, 47, 39, 910890), verbose_name='Data de Matrícula'),
        ),
        migrations.AlterField(
            model_name='instrutor',
            name='contato1',
            field=models.IntegerField(verbose_name='Contato Príncipal'),
        ),
        migrations.AlterField(
            model_name='instrutor',
            name='contato2',
            field=models.IntegerField(verbose_name='Contato Alternatico'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='duracao',
            field=models.CharField(choices=[('1', '1H'), ('2', '2H'), ('3', '2H30')], max_length=20, verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.CharField(choices=[('1', '07:00:00'), ('2', '16:00:00'), ('3', '20:00:00')], max_length=20, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='numero_aluno',
            field=models.IntegerField(verbose_name='Número de Alunos'),
        ),
    ]