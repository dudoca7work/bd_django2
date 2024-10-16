# seu_app/forms.py
from django import forms # type: ignore
from .models import usuario
from .models import inscricao
from .models import edital
from .models import bolsista_validado
from .models import convocacao
from .models import posse
from .models import dado_bancario
from .models import bolsista_ativo
from .models import frequencia
from .models import registro
from .models import consultapag

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'  # Ou especifique campos específicos



class inscricaoForm(forms.ModelForm):
    class Meta:
        model = inscricao
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class editalForm(forms.ModelForm):
    class Meta:
        model = edital
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class bolsista_validadoForm(forms.ModelForm):
    class Meta:
        model = bolsista_validado
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class convocacaoForm(forms.ModelForm):
    class Meta:
        model = convocacao
        fields = ['data_inicio', 'data_fim', 'edital', 'bolsista_validado']



class posseForm(forms.ModelForm):
    class Meta:
        model = posse
        fields = ['decla_anuencia', 'termo_disponibilidade', 'termo_compromisso', 'usuario', 'edital', 'convocacao']



class dado_bancarioForm(forms.ModelForm):
    class Meta:
        model = dado_bancario
        fields = ['pis_pasep', 'banco', 'conta', 'dig_v', 'tipo_conta', 'matricula', 'tipo_matricula', 'cpf_avaliador', 'posse']



class bolsista_ativoForm(forms.ModelForm):
    class Meta:
        model = bolsista_ativo
        fields = ['status', 'bolsista_validado', 'dados_bancarios']



class frequenciaForm(forms.ModelForm):
    class Meta:
        model = frequencia
        fields = ['mes', 'ano', 'carga_horaria', 'arquivo_freq', 'bolsista_validado', 'bolsista_ativo']



class registroForm(forms.ModelForm):
    class Meta:
        model = registro
        fields = ['turno', 'dias', 'carga_horaria', 'frequencia']



class consultapagForm(forms.ModelForm):
    class Meta:
        model = consultapag
        fields = ['status_pag', 'mes', 'etapas', 'processo', 'bolsista_validado', 'bolsista_ativo', 'frequencia']



