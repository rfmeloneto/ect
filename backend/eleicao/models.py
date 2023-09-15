from django.db import models


class Candidatos (models.Model):
    numero_candidato = models.PositiveIntegerField()
    votos = models.PositiveIntegerField()


class Urnas (models.Model):
    candidato = models.ManyToManyField(Candidatos)
    vqr = models.FloatField()
    vrch = models.CharField(max_length=100)
    orig = models.CharField(max_length=100)
    orlc = models.CharField(max_length=100)
    proc = models.CharField(max_length=100)
    dtpl = models.CharField(max_length=100)
    plei = models.CharField(max_length=100)
    turn = models.CharField(max_length=100)
    fase = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    seca = models.CharField(max_length=100)
    idue = models.CharField(max_length=100)
    idca = models.CharField(max_length=100)
    loca = models.CharField(max_length=100)
    apto = models.PositiveIntegerField()
    comp = models.PositiveIntegerField()
    falt = models.PositiveIntegerField()
    datab = models.CharField(max_length=100)
    hrab = models.CharField(max_length=100)
    dtfc = models.CharField(max_length=100)
    hrfc = models.CharField(max_length=100)
    idel = models.CharField(max_length=100)
    carg = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    verc = models.CharField(max_length=100)
    apta = models.PositiveIntegerField()
    nomi = models.PositiveIntegerField()
    bran = models.PositiveIntegerField()
    nulo = models.PositiveIntegerField()
    totc = models.PositiveIntegerField()
    hash = models.TextField()
    assi = models.TextField()


class Cidades(models.Model):
    muni = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, blank=True, null=True)
    urna = models.ManyToManyField(Urnas)


class Estado(models.Model):
    unfe = models.CharField(max_length=100)
    cidade = models.ManyToManyField(Cidades)
