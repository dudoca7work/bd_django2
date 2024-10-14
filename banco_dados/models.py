from django.db import models # type: ignore
from django.core.validators import MinLengthValidator, RegexValidator # type: ignore

class Usuario(models.Model):
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[
            RegexValidator(r'^\d{11}$', 'CPF must be 11 digits')
        ]
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

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    ESCOLARIDADE_CHOICES = (
        ('Superior', 'Superior'),
        ('Especialização', 'Especialização'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    )
    
    encargo = models.CharField(max_length=200, null=False)
    acao = models.CharField(max_length=200, null=False)
    inep = models.CharField(max_length=200, null=False)
    email_inst = models.EmailField(max_length=200, blank=False, null=False)
    endereco = models.CharField(max_length=200, null=False)
    n_endereco = models.IntegerField(null=False)
    bairro = models.CharField(max_length=200, null=False)
    municipio = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=200, null=False)
    cep = models.CharField(max_length=9, null=False, validators=[RegexValidator(r'^\d{5}-\d{3}$', 'CEP inválido')])
    escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADE_CHOICES, blank=False, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Edital(models.Model):
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
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)

class BolsistaValidado(models.Model):
    bolsistas_id = models.CharField(max_length=22, null=False)
    classificacao = models.IntegerField(blank=False)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)

class Convocacao(models.Model):
    data_inicio = models.DateField(blank=False)
    data_fim = models.DateField(blank=False)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    bolsista_validado = models.ForeignKey(BolsistaValidado, on_delete=models.CASCADE)

class Posse(models.Model):
    decla_anuencia = models.URLField(blank=False)
    termo_disponibilidade = models.URLField(blank=False)
    termo_compromisso = models.URLField(blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    convocacao = models.ForeignKey(Convocacao, on_delete=models.CASCADE)

class DadosBancarios(models.Model):
    dados_bancarios_id = models.AutoField(primary_key=True)
    pis_pasep = models.CharField(max_length=10)
    banco = models.CharField(max_length=200)
    conta = models.CharField(max_length=200)
    dig_v = models.CharField(max_length=20)
    tipo_conta = models.CharField(max_length=20)
    matricula = models.CharField(max_length=200)
    tipo_matricula = models.CharField(max_length=200)
    cpf_avaliador = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    posse = models.ForeignKey(Posse, on_delete=models.CASCADE)

class BolsistaAtivo(models.Model):
    status = models.CharField(max_length=200)
    bolsista_validado = models.ForeignKey(BolsistaValidado, on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(DadosBancarios, on_delete=models.CASCADE)

class Frequencia(models.Model):
    mes = models.IntegerField(blank=False)  # Alterado para IntegerField
    ano = models.IntegerField(blank=False)  # Alterado para IntegerField
    carga_horaria = models.CharField(max_length=200)
    arquivo_freq = models.FileField(upload_to='frequencias/')
    bolsista_validado = models.ForeignKey(BolsistaValidado, on_delete=models.CASCADE)
    bolsista_ativo = models.ForeignKey(BolsistaAtivo, on_delete=models.CASCADE)

class Registros(models.Model):
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
    etapas = models.CharField(max_length=200)
    processo = models.CharField(max_length=200)
    bolsista_validado = models.ForeignKey(BolsistaValidado, on_delete=models.CASCADE)
    bolsista_ativo = models.ForeignKey(BolsistaAtivo, on_delete=models.CASCADE)
    frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
