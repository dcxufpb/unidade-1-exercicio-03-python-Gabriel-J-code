import cupom;

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_loja_completa():
	assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
	
	cupom.nome_loja = ""
	assert cupom.imprime_dados_loja() == '''O campo nome da loja é obrigatório'''
	cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
	cupom.logradouro = ""
	assert cupom.imprime_dados_loja() == '''O campo logradouro do endereço é obrigatório'''
	cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
	cupom.numero = 0
	assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
	cupom.numero = 500

def test_municipio_vazio():
	cupom.municipio = ""
	assert cupom.imprime_dados_loja() == '''O campo município do endereço é obrigatório'''
	cupom.municipio = "Campinas"

def test_estado_vazio():
	cupom.estado = ""
	assert cupom.imprime_dados_loja() == '''O campo estado do endereço é obrigatório'''
	cupom.estado = "SP"

def test_cnpj_vazio():
	cupom.cnpj = ""
	assert cupom.imprime_dados_loja() == '''O campo CNPJ da loja é obrigatório'''
	cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazio():
	cupom.inscricao_estadual = ""
	assert cupom.imprime_dados_loja() == '''O campo inscrição estadual da loja é obrigatório'''
	cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
	# Defina seus próprios valores para as variáveis a seguir
	cupom.nome_loja = "Tropical"
	cupom.logradouro = "Rua siqueira Campos"
	cupom.numero = 580
	cupom.complemento = ""
	cupom.bairro = "Centro"
	cupom.municipio = "Paulista"
	cupom.estado = "Pernambuco"
	cupom.cep = "53401-320"
	cupom.telefone = "(81) 3438-5714"
	cupom.observacao = ""
	cupom.cnpj = "37.886.772/0001-82"
	cupom.inscricao_estadual = "4232303-79"

	#E atualize o texto esperado abaixo
	assert cupom.imprime_dados_loja() == '''Tropical
Rua siqueira Campos, 580
Centro - Paulista - Pernambuco
CEP:53401-320 Tel (81) 3438-5714

CNPJ: 37.886.772/0001-82
IE: 4232303-79
'''
	cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
	cupom.logradouro = "Av. Projetada Leste"
	cupom.numero = 500
	cupom.complemento = "EUC F32/33/34"
	cupom.bairro = "Br. Sta Genebra"
	cupom.municipio = "Campinas"
	cupom.estado = "SP"
	cupom.cep = "13080-395"
	cupom.telefone = "(19) 3756-7408"
	cupom.observacao = "Loja 1317 (PDP)"
	cupom.cnpj = "42.591.651/0797-34"
	cupom.inscricao_estadual = "244.898.500.113"
