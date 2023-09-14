from django.db import models


class Reserva(models.Model):
    cnpj = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome_empresa


class Stand(models.Model):
    localizacao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
