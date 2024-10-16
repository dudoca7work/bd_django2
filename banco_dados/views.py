from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import usuario, inscricao, edital, bolsista_validado, convocacao, posse, dado_bancario, bolsista_ativo, frequencia, registro, consultapag

# Views para o model Usuario
class UsuarioListView(ListView):
    model = usuario
    template_name = 'usuario_list.html'

class UsuarioDetailView(DetailView):
    model = usuario
    template_name = 'usuario_detail.html'

class UsuarioCreateView(CreateView):
    model = usuario
    fields = '__all__'
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioUpdateView(UpdateView):
    model = usuario
    fields = '__all__'
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(DeleteView):
    model = usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')

# Views para o model Inscricao
class InscricaoListView(ListView):
    model = inscricao
    template_name = 'inscricao_list.html'

class InscricaoDetailView(DetailView):
    model = inscricao
    template_name = 'inscricao_detail.html'

class InscricaoCreateView(CreateView):
    model = inscricao
    fields = '__all__'
    template_name = 'inscricao_form.html'
    success_url = reverse_lazy('inscricao-list')

class InscricaoUpdateView(UpdateView):
    model = inscricao
    fields = '__all__'
    template_name = 'inscricao_form.html'
    success_url = reverse_lazy('inscricao-list')

class InscricaoDeleteView(DeleteView):
    model = inscricao
    template_name = 'inscricao_confirm_delete.html'
    success_url = reverse_lazy('inscricao-list')

# Views para o model Edital
class EditalListView(ListView):
    model = edital
    template_name = 'edital_list.html'

class EditalDetailView(DetailView):
    model = edital
    template_name = 'edital_detail.html'

class EditalCreateView(CreateView):
    model = edital
    fields = '__all__'
    template_name = 'edital_form.html'
    success_url = reverse_lazy('edital-list')

class EditalUpdateView(UpdateView):
    model = edital
    fields = '__all__'
    template_name = 'edital_form.html'
    success_url = reverse_lazy('edital-list')

class EditalDeleteView(DeleteView):
    model = edital
    template_name = 'edital_confirm_delete.html'
    success_url = reverse_lazy('edital-list')

# Views para o model Bolsista Validado
class BolsistaValidadoListView(ListView):
    model = bolsista_validado
    template_name = 'bolsista_validado_list.html'

class BolsistaValidadoDetailView(DetailView):
    model = bolsista_validado
    template_name = 'bolsista_validado_detail.html'

class BolsistaValidadoCreateView(CreateView):
    model = bolsista_validado
    fields = '__all__'
    template_name = 'bolsista_validado_form.html'
    success_url = reverse_lazy('bolsista_validado-list')

class BolsistaValidadoUpdateView(UpdateView):
    model = bolsista_validado
    fields = '__all__'
    template_name = 'bolsista_validado_form.html'
    success_url = reverse_lazy('bolsista_validado-list')

class BolsistaValidadoDeleteView(DeleteView):
    model = bolsista_validado
    template_name = 'bolsista_validado_confirm_delete.html'
    success_url = reverse_lazy('bolsista_validado-list')

# Views para o model Convocacao
class ConvocacaoListView(ListView):
    model = convocacao
    template_name = 'convocacao_list.html'

class ConvocacaoDetailView(DetailView):
    model = convocacao
    template_name = 'convocacao_detail.html'

class ConvocacaoCreateView(CreateView):
    model = convocacao
    fields = '__all__'
    template_name = 'convocacao_form.html'
    success_url = reverse_lazy('convocacao-list')

class ConvocacaoUpdateView(UpdateView):
    model = convocacao
    fields = '__all__'
    template_name = 'convocacao_form.html'
    success_url = reverse_lazy('convocacao-list')

class ConvocacaoDeleteView(DeleteView):
    model = convocacao
    template_name = 'convocacao_confirm_delete.html'
    success_url = reverse_lazy('convocacao-list')

# Views para o model Posse
class PosseListView(ListView):
    model = posse
    template_name = 'posse_list.html'

class PosseDetailView(DetailView):
    model = posse
    template_name = 'posse_detail.html'

class PosseCreateView(CreateView):
    model = posse
    fields = '__all__'
    template_name = 'posse_form.html'
    success_url = reverse_lazy('posse-list')

class PosseUpdateView(UpdateView):
    model = posse
    fields = '__all__'
    template_name = 'posse_form.html'
    success_url = reverse_lazy('posse-list')

class PosseDeleteView(DeleteView):
    model = posse
    template_name = 'posse_confirm_delete.html'
    success_url = reverse_lazy('posse-list')

# Views para o model Dado Bancario
class DadoBancarioListView(ListView):
    model = dado_bancario
    template_name = 'dado_bancario_list.html'

class DadoBancarioDetailView(DetailView):
    model = dado_bancario
    template_name = 'dado_bancario_detail.html'

class DadoBancarioCreateView(CreateView):
    model = dado_bancario
    fields = '__all__'
    template_name = 'dado_bancario_form.html'
    success_url = reverse_lazy('dado_bancario-list')

class DadoBancarioUpdateView(UpdateView):
    model = dado_bancario
    fields = '__all__'
    template_name = 'dado_bancario_form.html'
    success_url = reverse_lazy('dado_bancario-list')

class DadoBancarioDeleteView(DeleteView):
    model = dado_bancario
    template_name = 'dado_bancario_confirm_delete.html'
    success_url = reverse_lazy('dado_bancario-list')

# Views para o model Bolsista Ativo
class BolsistaAtivoListView(ListView):
    model = bolsista_ativo
    template_name = 'bolsista_ativo_list.html'

class BolsistaAtivoDetailView(DetailView):
    model = bolsista_ativo
    template_name = 'bolsista_ativo_detail.html'

class BolsistaAtivoCreateView(CreateView):
    model = bolsista_ativo
    fields = '__all__'
    template_name = 'bolsista_ativo_form.html'
    success_url = reverse_lazy('bolsista_ativo-list')

class BolsistaAtivoUpdateView(UpdateView):
    model = bolsista_ativo
    fields = '__all__'
    template_name = 'bolsista_ativo_form.html'
    success_url = reverse_lazy('bolsista_ativo-list')

class BolsistaAtivoDeleteView(DeleteView):
    model = bolsista_ativo
    template_name = 'bolsista_ativo_confirm_delete.html'
    success_url = reverse_lazy('bolsista_ativo-list')

# Views para o model Frequencia
class FrequenciaListView(ListView):
    model = frequencia
    template_name = 'frequencia_list.html'

class FrequenciaDetailView(DetailView):
    model = frequencia
    template_name = 'frequencia_detail.html'

class FrequenciaCreateView(CreateView):
    model = frequencia
    fields = '__all__'
    template_name = 'frequencia_form.html'
    success_url = reverse_lazy('frequencia-list')

class FrequenciaUpdateView(UpdateView):
    model = frequencia
    fields = '__all__'
    template_name = 'frequencia_form.html'
    success_url = reverse_lazy('frequencia-list')

class FrequenciaDeleteView(DeleteView):
    model = frequencia
    template_name = 'frequencia_confirm_delete.html'
    success_url = reverse_lazy('frequencia-list')

# Views para o model Registro
class RegistroListView(ListView):
    model = registro
    template_name = 'registro_list.html'

class RegistroDetailView(DetailView):
    model = registro
    template_name = 'registro_detail.html'

class RegistroCreateView(CreateView):
    model = registro
    fields = '__all__'
    template_name = 'registro_form.html'
    success_url = reverse_lazy('registro-list')

class RegistroUpdateView(UpdateView):
    model = registro
    fields = '__all__'
    template_name = 'registro_form.html'
    success_url = reverse_lazy('registro-list')

class RegistroDeleteView(DeleteView):
    model = registro
    template_name = 'registro_confirm_delete.html'
    success_url = reverse_lazy('registro-list')

# Views para o model ConsultaPag
class consultapagListView(ListView):
    model = consultapag
    template_name = 'consulta_pag_list.html'

class consultapagDetailView(DetailView):
    model = consultapag
    template_name = 'consulta_pag_detail.html'

class consultapagCreateView(CreateView):
    model = consultapag
    fields = '__all__'
    template_name = 'consulta_pag_form.html'
    success_url = reverse_lazy('consulta_pag-list')

class consultapagUpdateView(UpdateView):
    model = consultapag
    fields = '__all__'
    template_name = 'consulta_pag_form.html'
    success_url = reverse_lazy('consulta_pag-list')

class consultapagDeleteView(DeleteView):
    model = consultapag
    template_name = 'consulta_pag_confirm_delete.html'
    success_url = reverse_lazy('consulta_pag-list')
