# Generated by Django 4.2.2 on 2023-07-04 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_alter_aluno_data_matricula_alter_aluno_documento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='instrutor',
            name='documento',
        ),
        migrations.AddField(
            model_name='aluno',
            name='bi',
            field=models.CharField(default=1, max_length=14, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrutor',
            name='bi',
            field=models.CharField(default=2, max_length=14, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_matricula',
            field=models.DateField(default=datetime.datetime(2023, 7, 4, 2, 59, 59, 455838), verbose_name='Data de Matrícula'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='duracao',
            field=models.CharField(choices=[('1H', '1H'), ('2H', '2H'), ('2H30', '2H30')], max_length=20, verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.CharField(choices=[('07:00:00', '07:00:00'), ('16:00:00', '16:00:00'), ('20:00:00', '20:00:00')], max_length=20, verbose_name='Horário'),
        ),
    ]
