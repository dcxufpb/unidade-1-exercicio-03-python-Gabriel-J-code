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

def imprime_dados_loja():
	#linha nome_loja
	if not nome_loja:
		return"O campo nome da loja é obrigatório"
	nota = nome_loja + "\n"

	#linha logradouro, numero, e complemento
	if not logradouro:
		return"O campo logradouro do endereço é obrigatório"
	
	_numero = "s/n" if not numero else str(numero)
	
	_complemento = " " + complemento if complemento else ""

	nota += "%s, %s%s\n" %(logradouro,_numero,_complemento)

	# linha bairro, municipio, e estado
	_bairro = bairro + " - " if bairro else ""

	if not municipio:
		return"O campo município do endereço é obrigatório"

	if not estado:
		return"O campo estado do endereço é obrigatório"
	
	nota += "%s%s - %s\n" % (_bairro,municipio,estado)

	#linha cep, e telefone
	_cep = "CEP:" + cep if cep else ""
	
	_telefone = "Tel " + telefone if telefone else ""
	
	_telefone = " " + _telefone if cep and telefone else _telefone

	nota += "%s%s\n" % (_cep,_telefone)

	#linha observacao
	nota += observacao + "\n"

	#linha cnpj
	if not cnpj:
		return"O campo CNPJ da loja é obrigatório"
	nota += "CNPJ: %s\n" %(cnpj)
	
	#linha inscricao_estadual
	if not inscricao_estadual:
		return"O campo inscrição estadual da loja é obrigatório"
	nota += "IE: %s\n" % (inscricao_estadual)

	return nota
