# seu_app/forms.py
from django import forms # type: ignore
from .models import Usuario
from .models import Inscricao
from .models import Edital
from .models import BolsistaValidado
from .models import Convocacao
from .models import Posse
from .models import DadosBancarios
from .models import BolsistaAtivo
from .models import Frequencia
from .models import Registros
from .models import ConsultaPag

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'  # Ou especifique campos específicos



class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class BolsistaValidadoForm(forms.ModelForm):
    class Meta:
        model = BolsistaValidado
        fields = '__all__'  # Isso irá gerar um formulário com todos os campos



class ConvocacaoForm(forms.ModelForm):
    class Meta:
        model = Convocacao
        fields = ['data_inicio', 'data_fim', 'edital', 'bolsista_validado']



class PosseForm(forms.ModelForm):
    class Meta:
        model = Posse
        fields = ['decla_anuencia', 'termo_disponibilidade', 'termo_compromisso', 'usuario', 'edital', 'convocacao']



class DadosBancariosForm(forms.ModelForm):
    class Meta:
        model = DadosBancarios
        fields = ['pis_pasep', 'banco', 'conta', 'dig_v', 'tipo_conta', 'matricula', 'tipo_matricula', 'cpf_avaliador', 'posse']



class BolsistaAtivoForm(forms.ModelForm):
    class Meta:
        model = BolsistaAtivo
        fields = ['status', 'bolsista_validado', 'dados_bancarios']



class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['mes', 'ano', 'carga_horaria', 'arquivo_freq', 'bolsista_validado', 'bolsista_ativo']



class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = ['turno', 'dias', 'carga_horaria', 'frequencia']



class ConsultaPagForm(forms.ModelForm):
    class Meta:
        model = ConsultaPag
        fields = ['status_pag', 'mes', 'etapas', 'processo', 'bolsista_validado', 'bolsista_ativo', 'frequencia']



