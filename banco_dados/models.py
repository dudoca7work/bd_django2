from django.db import models # type: ignore
from django.core.validators import MinLengthValidator, RegexValidator # type: ignore


class usuario(models.Model):
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[
            RegexValidator(r'^\d{11}$', 'CPF must be 11 digits')
        ]
    )
    ESCOLARIDADE_CHOICES = (
        ('Superior', 'Superior'),
        ('Especialização', 'Especialização'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    )
    senha = models.CharField(max_length=128, blank=False, null=False)
    nome = models.CharField(max_length=200, null=False)
    orgao_emissor = models.CharField(max_length=200, null=False)
    data_emissao = models.DateField(null=False)
    data_nasc = models.DateField(null=False)
    nome_mae = models.CharField(max_length=200, null=False)
    tel1 = models.CharField(max_length=13, blank=False, null=False)
    tel2 = models.CharField(max_length=13, blank=True, null=True)
    email1 = models.EmailField(max_length=200, blank=False, null=False)
    email2 = models.EmailField(max_length=200, blank=True, null=True)
    endereco = models.CharField(max_length=200, null=False)
    n_endereco = models.IntegerField(null=False)
    bairro = models.CharField(max_length=200, null=False)
    municipio = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=200, null=False)
    cep = models.CharField(max_length=9, null=False, validators=[RegexValidator(r'^\d{5}-\d{3}$', 'CEP inválido')])
    escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADE_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome

class inscricao(models.Model):
    encargo = models.CharField(max_length=200, null=False)
    acao = models.CharField(max_length=200, null=False)
    edital_id = models.CharField(max_length=20, null=False)
    encargo = models.CharField(max_length=200, null=False)
    crit_a = models.CharField(max_length=200, null=False)
    crit_b = models.CharField(max_length=200, null=False)
    crit_c = models.CharField(max_length=200, null=False)
    crit_d = models.CharField(max_length=200, null=False)
    crit_e = models.CharField(max_length=200, null=False)
    crit_f = models.CharField(max_length=200, null=False)
    crit_g = models.CharField(max_length=200, null=False)
    crit_h = models.CharField(max_length=200, null=False)
    crit_i = models.CharField(max_length=200, null=False)
    crit_j = models.CharField(max_length=200, null=False)


class edital(models.Model):
    STATUS_VIGENCIA_CHOICES = (
        ('A', 'Ativo'),
        ('P', 'Pendente'),
    )
    
    edital_id = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=200, null=False)
    acao = models.CharField(max_length=200, null=False)
    programa = models.CharField(max_length=200, null=False)
    ano = models.IntegerField(blank=False)
    inicio_vigencia = models.DateField(blank=False)
    termino_vigencia = models.DateField(blank=False)
    prazo_bolsa = models.DurationField(null=False)
    status_vigencia = models.CharField(max_length=1, choices=STATUS_VIGENCIA_CHOICES, blank=False, null=False)
    tipo = models.CharField(max_length=200, null=False)
    inscricao = models.ForeignKey(inscricao, on_delete=models.CASCADE)

class bolsista_validado(models.Model):
    bolsistas_id = models.CharField(max_length=22, null=False)
    edital_id = models.CharField(max_length=20, null=False)
    classificacao_1 = models.IntegerField(blank=False)
    classificacao_2 = models.IntegerField(blank=False)
    classificacao_3 = models.IntegerField(blank=False)
    pcd = models.CharField(max_length=200, null=False)
    

class convocacao(models.Model):
    data_inicio = models.DateField(blank=False)
    data_fim = models.DateField(blank=False)
    edital = models.ForeignKey(edital, on_delete=models.CASCADE)
    bolsista_validado = models.ForeignKey(bolsistavalidado, on_delete=models.CASCADE)

class posse(models.Model):
    decla_anuencia = models.URLField(blank=False)
    bolsistas_id = models.CharField(max_length=22, null=False)
    termo_compromisso = models.URLField(blank=False)
    termo_disponibilidade = models.URLField(blank=False)
    convocacao = models.ForeignKey(Convocacao, on_delete=models.CASCADE)

class dado_bancario(models.Model):
    dado_bancario_id = models.AutoField(primary_key=True)
    pis_pasep = models.CharField(max_length=10)
    banco = models.CharField(max_length=200)
    conta = models.CharField(max_length=200)
    dig_v = models.CharField(max_length=20)
    tipo_conta = models.CharField(max_length=20)
    matricula = models.CharField(max_length=200)
    tipo_matricula = models.CharField(max_length=200)
    cpf_avaliador = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    posse = models.ForeignKey(posse, on_delete=models.CASCADE)

class bolsista_ativo(models.Model):
    status = models.CharField(max_length=200)
    bolsista_validado = models.ForeignKey(bolsista_validado, on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(dado_bancario, on_delete=models.CASCADE)

class frequencia(models.Model):
    mes = models.IntegerField(blank=False)  # Alterado para IntegerField
    ano = models.IntegerField(blank=False)  # Alterado para IntegerField
    carga_horaria = models.CharField(max_length=200)
    arquivo_freq = models.FileField(upload_to='frequencias/')
    bolsista_validado = models.ForeignKey(bolsistavalidado, on_delete=models.CASCADE)
    bolsista_ativo = models.ForeignKey(bolsistaativo, on_delete=models.CASCADE)

class registro(models.Model):
    TURNO_CHOICES = (
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    )
    CARGA_HORARIA_CHOICES = (
        ('3 Horas', '3 Horas'),
        ('4 Horas', '4 Horas'),
    )

    turno = models.CharField(max_length=6, choices=TURNO_CHOICES, blank=False, null=False)  # Alterado max_length
    dias = models.IntegerField(null=False)  # Alterado para IntegerField
    carga_horaria = models.CharField(max_length=8, choices=CARGA_HORARIA_CHOICES, blank=False, null=False)  # Alterado max_length
    frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)

class ConsultaPag(models.Model):
    STATUS_PAG_CHOICES = (
        ('A', 'Ativo'),
        ('P', 'Pendente'),
    )
    
    status_pag = models.CharField(max_length=1, choices=STATUS_PAG_CHOICES, blank=False)
    mes = models.IntegerField(blank=False)  # Alterado para IntegerField
    etapa = models.CharField(max_length=200)
    processo = models.CharField(max_length=200)
    bolsista_validado = models.ForeignKey(bolsistavalidado, on_delete=models.CASCADE)
    bolsista_ativo = models.ForeignKey(bolsistaativo, on_delete=models.CASCADE)