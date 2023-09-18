from django.db import models


class ProcessoEleitoral(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    is_valid = models.BooleanField()

    class Meta:
        verbose_name = 'Processo Eleitoral'
        verbose_name_plural = 'Processos Eleitorais'

    def __str__(self):
        return f"Processo {self.numero}"


class Candidatos (models.Model):
    numero_candidato = models.PositiveIntegerField()
    votos = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def __str__(self):
        return f"Numero do Candidato: {self.numero_candidato}"


class Urnas (models.Model):
    processo_eleitoral = models.ForeignKey(
        ProcessoEleitoral, on_delete=models.PROTECT)
    candidato = models.ManyToManyField(Candidatos)
    vqr = models.CharField(max_length=100)
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
    apto = models.CharField(max_length=100)
    comp = models.CharField(max_length=100)
    falt = models.CharField(max_length=100)
    datab = models.CharField(max_length=100)
    hrab = models.CharField(max_length=100)
    dtfc = models.CharField(max_length=100)
    hrfc = models.CharField(max_length=100)
    idel = models.CharField(max_length=100)
    carg = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    verc = models.CharField(max_length=100)
    apta = models.CharField(max_length=100)
    nomi = models.CharField(max_length=100)
    bran = models.CharField(max_length=100)
    nulo = models.CharField(max_length=100)
    totc = models.CharField(max_length=100)
    hash = models.TextField()
    assi = models.TextField()

    def __str__(self):
        return f"{self.processo_eleitoral.nome} - {self.zona} - {self.idue}"

    class Meta:
        verbose_name = 'Urna'
        verbose_name_plural = 'Urnas'


class Cidades(models.Model):
    muni = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, blank=True, null=True)
    urna = models.ManyToManyField(Urnas)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


class Estado(models.Model):
    unfe = models.CharField(max_length=100)
    cidade = models.ManyToManyField(Cidades)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
