from django.urls import path # type: ignore
from . import views

urlpatterns = [
    # URLs para Usuario
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/novo/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/editar/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/deletar/', views.usuario_delete, name='usuario_delete'),
    # Repita para outras models...
]

urlpatterns = [
    # URLs para Inscricao
    path('inscricoes/', views.inscricao_list, name='inscricao_list'),  # Listar inscrições
    path('inscricoes/<int:pk>/', views.inscricao_detail, name='inscricao_detail'),  # Detalhar inscrição
    path('inscricoes/nova/', views.inscricao_create, name='inscricao_create'),  # Criar nova inscrição
    path('inscricoes/<int:pk>/editar/', views.inscricao_update, name='inscricao_update'),  # Editar inscrição existente
    path('inscricoes/<int:pk>/deletar/', views.inscricao_delete, name='inscricao_delete'),  # Deletar inscrição existente
]

urlpatterns = [
    # URLs para Edital
    path('editais/', views.edital_list, name='edital_list'),  # Listar editais
    path('editais/<int:pk>/', views.edital_detail, name='edital_detail'),  # Detalhar edital
    path('editais/novo/', views.edital_create, name='edital_create'),  # Criar novo edital
    path('editais/<int:pk>/editar/', views.edital_update, name='edital_update'),  # Editar edital existente
    path('editais/<int:pk>/deletar/', views.edital_delete, name='edital_delete'),  # Deletar edital existente
]

urlpatterns = [
    # URLs para BolsistaValidado
    path('bolsistas-validados/', views.bolsista_validado_list, name='bolsista_validado_list'),  # Listar bolsistas validados
    path('bolsistas-validados/<int:pk>/', views.bolsista_validado_detail, name='bolsista_validado_detail'),  # Detalhar bolsista validado
    path('bolsistas-validados/novo/', views.bolsista_validado_create, name='bolsista_validado_create'),  # Criar novo bolsista validado
    path('bolsistas-validados/<int:pk>/editar/', views.bolsista_validado_update, name='bolsista_validado_update'),  # Editar bolsista validado
    path('bolsistas-validados/<int:pk>/deletar/', views.bolsista_validado_delete, name='bolsista_validado_delete'),  # Deletar bolsista validado
]

urlpatterns = [
    # URLs para Convocacao
    path('convocacoes/', views.convocacao_list, name='convocacao_list'),  # Listar convocacoes
    path('convocacoes/<int:pk>/', views.convocacao_detail, name='convocacao_detail'),  # Detalhar convocacao
    path('convocacoes/novo/', views.convocacao_create, name='convocacao_create'),  # Criar nova convocacao
    path('convocacoes/<int:pk>/editar/', views.convocacao_update, name='convocacao_update'),  # Editar convocacao existente
    path('convocacoes/<int:pk>/deletar/', views.convocacao_delete, name='convocacao_delete'),  # Deletar convocacao existente
]

urlpatterns = [
    # URLs para Posse
    path('posses/', views.posse_list, name='posse_list'),  # Listar posses
    path('posses/<int:pk>/', views.posse_detail, name='posse_detail'),  # Detalhar posse
    path('posses/novo/', views.posse_create, name='posse_create'),  # Criar nova posse
    path('posses/<int:pk>/editar/', views.posse_update, name='posse_update'),  # Editar posse existente
    path('posses/<int:pk>/deletar/', views.posse_delete, name='posse_delete'),  # Deletar posse existente
]

urlpatterns = [
    # URLs para DadosBancarios
    path('dados-bancarios/', views.dados_bancarios_list, name='dados_bancarios_list'),  # Listar dados bancários
    path('dados-bancarios/<int:pk>/', views.dados_bancarios_detail, name='dados_bancarios_detail'),  # Detalhar dados bancários
    path('dados-bancarios/novo/', views.dados_bancarios_create, name='dados_bancarios_create'),  # Criar novo dado bancário
    path('dados-bancarios/<int:pk>/editar/', views.dados_bancarios_update, name='dados_bancarios_update'),  # Editar dado bancário existente
    path('dados-bancarios/<int:pk>/deletar/', views.dados_bancarios_delete, name='dados_bancarios_delete'),  # Deletar dado bancário existente
]

urlpatterns = [
    # URLs para BolsistaAtivo
    path('bolsistas-ativos/', views.bolsista_ativo_list, name='bolsista_ativo_list'),  # Listar bolsistas ativos
    path('bolsistas-ativos/<int:pk>/', views.bolsista_ativo_detail, name='bolsista_ativo_detail'),  # Detalhar bolsista ativo
    path('bolsistas-ativos/novo/', views.bolsista_ativo_create, name='bolsista_ativo_create'),  # Criar novo bolsista ativo
    path('bolsistas-ativos/<int:pk>/editar/', views.bolsista_ativo_update, name='bolsista_ativo_update'),  # Editar bolsista ativo existente
    path('bolsistas-ativos/<int:pk>/deletar/', views.bolsista_ativo_delete, name='bolsista_ativo_delete'),  # Deletar bolsista ativo existente
]

urlpatterns = [
    # URLs para Frequencia
    path('frequencias/', views.frequencia_list, name='frequencia_list'),  # Listar frequências
    path('frequencias/<int:pk>/', views.frequencia_detail, name='frequencia_detail'),  # Detalhar frequência
    path('frequencias/novo/', views.frequencia_create, name='frequencia_create'),  # Criar nova frequência
    path('frequencias/<int:pk>/editar/', views.frequencia_update, name='frequencia_update'),  # Editar frequência existente
    path('frequencias/<int:pk>/deletar/', views.frequencia_delete, name='frequencia_delete'),  # Deletar frequência existente
]

urlpatterns = [
    # URLs para Registros
    path('registros/', views.registro_list, name='registro_list'),  # Listar registros
    path('registros/<int:pk>/', views.registro_detail, name='registro_detail'),  # Detalhar registro
    path('registros/novo/', views.registro_create, name='registro_create'),  # Criar novo registro
    path('registros/<int:pk>/editar/', views.registro_update, name='registro_update'),  # Editar registro existente
    path('registros/<int:pk>/deletar/', views.registro_delete, name='registro_delete'),  # Deletar registro existente
]

urlpatterns = [
    # URLs para ConsultaPag
    path('consultas-pagamento/', views.consulta_pag_list, name='consulta_pag_list'),  # Listar consultas de pagamento
    path('consultas-pagamento/<int:pk>/', views.consulta_pag_detail, name='consulta_pag_detail'),  # Detalhar consulta de pagamento
    path('consultas-pagamento/novo/', views.consulta_pag_create, name='consulta_pag_create'),  # Criar nova consulta de pagamento
    path('consultas-pagamento/<int:pk>/editar/', views.consulta_pag_update, name='consulta_pag_update'),  # Editar consulta de pagamento existente
    path('consultas-pagamento/<int:pk>/deletar/', views.consulta_pag_delete, name='consulta_pag_delete'),  # Deletar consulta de pagamento existente
]
