from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    class Meta:
        db_table = "Pessoa_pessoas" 

    def __str__(self):
        return self.nome
