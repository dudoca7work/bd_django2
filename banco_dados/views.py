# seu_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm
from .models import Inscricao
from .forms import InscricaoForm
from .models import Edital
from .forms import EditalForm
from .models import BolsistaValidado
from .forms import BolsistaValidadoForm
from .models import Convocacao
from .forms import ConvocacaoForm
from .models import Posse
from .forms import PosseForm
from .models import DadosBancarios
from .forms import DadosBancariosForm
from .models import BolsistaAtivo
from .forms import BolsistaAtivoForm
from .models import Frequencia
from .forms import FrequenciaForm
from .models import Registros
from .forms import RegistrosForm
from .models import ConsultaPag
from .forms import ConsultaPagForm

# View para listar usuários
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {'usuarios': usuarios})

# View para detalhes do usuário
def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuarios/usuario_detail.html', {'usuario': usuario})

# View para criar usuário
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

# View para editar usuário
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_detail', pk=pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

# View para deletar usuário
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})





# View para listar inscrições
def inscricao_list(request):
    inscricoes = Inscricao.objects.all()
    return render(request, 'inscricoes/inscricao_list.html', {'inscricoes': inscricoes})

# View para detalhes de uma inscrição
def inscricao_detail(request, pk):
    inscricao = get_object_or_404(Inscricao, pk=pk)
    return render(request, 'inscricoes/inscricao_detail.html', {'inscricao': inscricao})

# View para criar uma nova inscrição
def inscricao_create(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscricao_list')
    else:
        form = InscricaoForm()
    return render(request, 'inscricoes/inscricao_form.html', {'form': form})

# View para editar uma inscrição
def inscricao_update(request, pk):
    inscricao = get_object_or_404(Inscricao, pk=pk)
    if request.method == 'POST':
        form = InscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('inscricao_detail', pk=pk)
    else:
        form = InscricaoForm(instance=inscricao)
    return render(request, 'inscricoes/inscricao_form.html', {'form': form})

# View para deletar uma inscrição
def inscricao_delete(request, pk):
    inscricao = get_object_or_404(Inscricao, pk=pk)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('inscricao_list')
    return render(request, 'inscricoes/inscricao_confirm_delete.html', {'inscricao': inscricao})





# View para listar editais
def edital_list(request):
    editais = Edital.objects.all()
    return render(request, 'editais/edital_list.html', {'editais': editais})

# View para detalhes de um edital
def edital_detail(request, pk):
    edital = get_object_or_404(Edital, pk=pk)
    return render(request, 'editais/edital_detail.html', {'edital': edital})

# View para criar um novo edital
def edital_create(request):
    if request.method == 'POST':
        form = EditalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edital_list')
    else:
        form = EditalForm()
    return render(request, 'editais/edital_form.html', {'form': form})

# View para editar um edital existente
def edital_update(request, pk):
    edital = get_object_or_404(Edital, pk=pk)
    if request.method == 'POST':
        form = EditalForm(request.POST, instance=edital)
        if form.is_valid():
            form.save()
            return redirect('edital_detail', pk=pk)
    else:
        form = EditalForm(instance=edital)
    return render(request, 'editais/edital_form.html', {'form': form})

# View para deletar um edital
def edital_delete(request, pk):
    edital = get_object_or_404(Edital, pk=pk)
    if request.method == 'POST':
        edital.delete()
        return redirect('edital_list')
    return render(request, 'editais/edital_confirm_delete.html', {'edital': edital})





# View para listar bolsistas validados
def bolsista_validado_list(request):
    bolsistas = BolsistaValidado.objects.all()
    return render(request, 'bolsistas_validado/bolsista_validado_list.html', {'bolsistas': bolsistas})

# View para detalhes de um bolsista validado
def bolsista_validado_detail(request, pk):
    bolsista = get_object_or_404(BolsistaValidado, pk=pk)
    return render(request, 'bolsistas_validado/bolsista_validado_detail.html', {'bolsista': bolsista})

# View para criar um novo bolsista validado
def bolsista_validado_create(request):
    if request.method == 'POST':
        form = BolsistaValidadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bolsista_validado_list')
    else:
        form = BolsistaValidadoForm()
    return render(request, 'bolsistas_validado/bolsista_validado_form.html', {'form': form})

# View para editar um bolsista validado existente
def bolsista_validado_update(request, pk):
    bolsista = get_object_or_404(BolsistaValidado, pk=pk)
    if request.method == 'POST':
        form = BolsistaValidadoForm(request.POST, instance=bolsista)
        if form.is_valid():
            form.save()
            return redirect('bolsista_validado_detail', pk=pk)
    else:
        form = BolsistaValidadoForm(instance=bolsista)
    return render(request, 'bolsistas_validado/bolsista_validado_form.html', {'form': form})

# View para deletar um bolsista validado
def bolsista_validado_delete(request, pk):
    bolsista = get_object_or_404(BolsistaValidado, pk=pk)
    if request.method == 'POST':
        bolsista.delete()
        return redirect('bolsista_validado_list')
    return render(request, 'bolsistas_validado/bolsista_validado_confirm_delete.html', {'bolsista': bolsista})





# View para listar convocações
def convocacao_list(request):
    convocs = Convocacao.objects.all()
    return render(request, 'convocacoes/convocacao_list.html', {'convocs': convocs})

# View para detalhes de uma convocação
def convocacao_detail(request, pk):
    convoc = get_object_or_404(Convocacao, pk=pk)
    return render(request, 'convocacoes/convocacao_detail.html', {'convoc': convoc})

# View para criar uma nova convocação
def convocacao_create(request):
    if request.method == 'POST':
        form = ConvocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('convocacao_list')
    else:
        form = ConvocacaoForm()
    return render(request, 'convocacoes/convocacao_form.html', {'form': form})

# View para editar uma convocação existente
def convocacao_update(request, pk):
    convoc = get_object_or_404(Convocacao, pk=pk)
    if request.method == 'POST':
        form = ConvocacaoForm(request.POST, instance=convoc)
        if form.is_valid():
            form.save()
            return redirect('convocacao_detail', pk=pk)
    else:
        form = ConvocacaoForm(instance=convoc)
    return render(request, 'convocacoes/convocacao_form.html', {'form': form})

# View para deletar uma convocação
def convocacao_delete(request, pk):
    convoc = get_object_or_404(Convocacao, pk=pk)
    if request.method == 'POST':
        convoc.delete()
        return redirect('convocacao_list')
    return render(request, 'convocacoes/convocacao_confirm_delete.html', {'convoc': convoc})






# View para listar posses
def posse_list(request):
    posses = Posse.objects.all()
    return render(request, 'posses/posse_list.html', {'posses': posses})

# View para detalhes de uma posse
def posse_detail(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    return render(request, 'posses/posse_detail.html', {'posse': posse})

# View para criar uma nova posse
def posse_create(request):
    if request.method == 'POST':
        form = PosseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posse_list')
    else:
        form = PosseForm()
    return render(request, 'posses/posse_form.html', {'form': form})

# View para editar uma posse existente
def posse_update(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    if request.method == 'POST':
        form = PosseForm(request.POST, instance=posse)
        if form.is_valid():
            form.save()
            return redirect('posse_detail', pk=pk)
    else:
        form = PosseForm(instance=posse)
    return render(request, 'posses/posse_form.html', {'form': form})

# View para deletar uma posse
def posse_delete(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    if request.method == 'POST':
        posse.delete()
        return redirect('posse_list')
    return render(request, 'posses/posse_confirm_delete.html', {'posse': posse})







# View para listar dados bancários
def dadosbancarios_list(request):
    dados_bancarios = DadosBancarios.objects.all()
    return render(request, 'dadosbancarios/dadosbancarios_list.html', {'dados_bancarios': dados_bancarios})

# View para detalhes de dados bancários
def dadosbancarios_detail(request, pk):
    dado_bancario = get_object_or_404(DadosBancarios, pk=pk)
    return render(request, 'dadosbancarios/dadosbancarios_detail.html', {'dado_bancario': dado_bancario})

# View para criar um novo dado bancário
def dadosbancarios_create(request):
    if request.method == 'POST':
        form = DadosBancariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dadosbancarios_list')
    else:
        form = DadosBancariosForm()
    return render(request, 'dadosbancarios/dadosbancarios_form.html', {'form': form})

# View para editar um dado bancário existente
def dadosbancarios_update(request, pk):
    dado_bancario = get_object_or_404(DadosBancarios, pk=pk)
    if request.method == 'POST':
        form = DadosBancariosForm(request.POST, instance=dado_bancario)
        if form.is_valid():
            form.save()
            return redirect('dadosbancarios_detail', pk=pk)
    else:
        form = DadosBancariosForm(instance=dado_bancario)
    return render(request, 'dadosbancarios/dadosbancarios_form.html', {'form': form})

# View para deletar um dado bancário
def dadosbancarios_delete(request, pk):
    dado_bancario = get_object_or_404(DadosBancarios, pk=pk)
    if request.method == 'POST':
        dado_bancario.delete()
        return redirect('dadosbancarios_list')
    return render(request, 'dadosbancarios/dadosbancarios_confirm_delete.html', {'dado_bancario': dado_bancario})








# View para listar bolsistas ativos
def bolsistaativo_list(request):
    bolsistas_ativos = BolsistaAtivo.objects.all()
    return render(request, 'bolsistaativo/bolsistaativo_list.html', {'bolsistas_ativos': bolsistas_ativos})

# View para detalhes de um bolsista ativo
def bolsistaativo_detail(request, pk):
    bolsista_ativo = get_object_or_404(BolsistaAtivo, pk=pk)
    return render(request, 'bolsistaativo/bolsistaativo_detail.html', {'bolsista_ativo': bolsista_ativo})

# View para criar um novo bolsista ativo
def bolsistaativo_create(request):
    if request.method == 'POST':
        form = BolsistaAtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bolsistaativo_list')
    else:
        form = BolsistaAtivoForm()
    return render(request, 'bolsistaativo/bolsistaativo_form.html', {'form': form})

# View para editar um bolsista ativo existente
def bolsistaativo_update(request, pk):
    bolsista_ativo = get_object_or_404(BolsistaAtivo, pk=pk)
    if request.method == 'POST':
        form = BolsistaAtivoForm(request.POST, instance=bolsista_ativo)
        if form.is_valid():
            form.save()
            return redirect('bolsistaativo_detail', pk=pk)
    else:
        form = BolsistaAtivoForm(instance=bolsista_ativo)
    return render(request, 'bolsistaativo/bolsistaativo_form.html', {'form': form})

# View para deletar um bolsista ativo
def bolsistaativo_delete(request, pk):
    bolsista_ativo = get_object_or_404(BolsistaAtivo, pk=pk)
    if request.method == 'POST':
        bolsista_ativo.delete()
        return redirect('bolsistaativo_list')
    return render(request, 'bolsistaativo/bolsistaativo_confirm_delete.html', {'bolsista_ativo': bolsista_ativo})







# View para listar frequências
def frequencia_list(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'frequencia/frequencia_list.html', {'frequencias': frequencias})

# View para detalhes de uma frequência
def frequencia_detail(request, pk):
    frequencia = get_object_or_404(Frequencia, pk=pk)
    return render(request, 'frequencia/frequencia_detail.html', {'frequencia': frequencia})

# View para criar uma nova frequência
def frequencia_create(request):
    if request.method == 'POST':
        form = FrequenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('frequencia_list')
    else:
        form = FrequenciaForm()
    return render(request, 'frequencia/frequencia_form.html', {'form': form})

# View para editar uma frequência existente
def frequencia_update(request, pk):
    frequencia = get_object_or_404(Frequencia, pk=pk)
    if request.method == 'POST':
        form = FrequenciaForm(request.POST, request.FILES, instance=frequencia)
        if form.is_valid():
            form.save()
            return redirect('frequencia_detail', pk=pk)
    else:
        form = FrequenciaForm(instance=frequencia)
    return render(request, 'frequencia/frequencia_form.html', {'form': form})

# View para deletar uma frequência
def frequencia_delete(request, pk):
    frequencia = get_object_or_404(Frequencia, pk=pk)
    if request.method == 'POST':
        frequencia.delete()
        return redirect('frequencia_list')
    return render(request, 'frequencia/frequencia_confirm_delete.html', {'frequencia': frequencia})







# View para listar registros
def registro_list(request):
    registros = Registros.objects.all()  # Busca todos os registros
    return render(request, 'registros/registro_list.html', {'registros': registros})

# View para detalhes de um registro
def registro_detail(request, pk):
    registro = get_object_or_404(Registros, pk=pk)  # Busca um registro específico
    return render(request, 'registros/registro_detail.html', {'registro': registro})

# View para criar um novo registro
def registro_create(request):
    if request.method == 'POST':
        form = RegistrosForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo registro
            return redirect('registro_list')  # Redireciona para a lista de registros
    else:
        form = RegistrosForm()  # Cria um novo formulário
    return render(request, 'registros/registro_form.html', {'form': form})

# View para editar um registro existente
def registro_update(request, pk):
    registro = get_object_or_404(Registros, pk=pk)  # Busca o registro para edição
    if request.method == 'POST':
        form = RegistrosForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('registro_detail', pk=pk)  # Redireciona para os detalhes do registro
    else:
        form = RegistrosForm(instance=registro)  # Carrega o formulário com os dados existentes
    return render(request, 'registros/registro_form.html', {'form': form})

# View para deletar um registro
def registro_delete(request, pk):
    registro = get_object_or_404(Registros, pk=pk)  # Busca o registro para deletar
    if request.method == 'POST':
        registro.delete()  # Deleta o registro
        return redirect('registro_list')  # Redireciona para a lista de registros
    return render(request, 'registros/registro_confirm_delete.html', {'registro': registro})










# View para listar consultas de pagamento
def consulta_pag_list(request):
    consultas = ConsultaPag.objects.all()  # Busca todas as consultas de pagamento
    return render(request, 'consultas_pag/consulta_pag_list.html', {'consultas': consultas})

# View para detalhes de uma consulta de pagamento
def consulta_pag_detail(request, pk):
    consulta = get_object_or_404(ConsultaPag, pk=pk)  # Busca uma consulta específica
    return render(request, 'consultas_pag/consulta_pag_detail.html', {'consulta': consulta})

# View para criar uma nova consulta de pagamento
def consulta_pag_create(request):
    if request.method == 'POST':
        form = ConsultaPagForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova consulta
            return redirect('consulta_pag_list')  # Redireciona para a lista de consultas
    else:
        form = ConsultaPagForm()  # Cria um novo formulário
    return render(request, 'consultas_pag/consulta_pag_form.html', {'form': form})

# View para editar uma consulta de pagamento existente
def consulta_pag_update(request, pk):
    consulta = get_object_or_404(ConsultaPag, pk=pk)  # Busca a consulta para edição
    if request.method == 'POST':
        form = ConsultaPagForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('consulta_pag_detail', pk=pk)  # Redireciona para os detalhes da consulta
    else:
        form = ConsultaPagForm(instance=consulta)  # Carrega o formulário com os dados existentes
    return render(request, 'consultas_pag/consulta_pag_form.html', {'form': form})

# View para deletar uma consulta de pagamento
def consulta_pag_delete(request, pk):
    consulta = get_object_or_404(ConsultaPag, pk=pk)  # Busca a consulta para deletar
    if request.method == 'POST':
        consulta.delete()  # Deleta a consulta
        return redirect('consulta_pag_list')  # Redireciona para a lista de consultas
    return render(request, 'consultas_pag/consulta_pag_confirm_delete.html', {'consulta': consulta})
