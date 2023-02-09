class Apresentacao:
	def __init__(self):
		pass

	def menu_inicial(self):
		print("\n\n\t\t\tCATALOGO DE PRODUTOS DE INVESTIMENTO")
		print("\t1. Acessar produtos de investimento")
		print("\t2. Cadastrar")
		print("\t3. Autenticar")
		print("\t4. Sair")

		opcao = int(input())
		return opcao

	def menu_produtos(self):
		print("\t1. Tesouro Direto")
		print("\t2. Fundo de Investimento")
		print("\t3. Renda Fixa e Variavel")

		opcao = int(input())
		return opcao

	def menu_cadastrar(self):
		informacoes = {}

		print("Informe sua identidade")
		identidade = input()
		informacoes.update({"identidade": identidade})

		print("Informe seu nome")
		nome = input()
		informacoes.update({"nome": nome})

		print("Informe sua data de nascimento")
		data_nascimento = input()
		informacoes.update({"data_nascimento": data_nascimento})

		print("Informe sua renda mensal")
		renda_mensal = float(input())
		informacoes.update({"renda_mensal": renda_mensal})

		print("Cidade: ")
		cidade = input()
		informacoes.update({"cidade": cidade})

		print("Bairro:")
		bairro = input()
		informacoes.update({"bairro": bairro})

		print("Rua")
		rua = input()
		informacoes.update({"rua": rua})

		print("Numero da casa ou apartamento")
		numero = input()
		informacoes.update({"numero": numero})

		telefones = []
		print("Quantos telefones deseja adicionar?")
		qtd_telefone = int(input())
		for i in range(qtd_telefone):
			telefone = input()
			telefones.append(telefone)

		informacoes.update({"telefones": telefones})

		print("Informe seu cep")
		cep = input()
		informacoes.update({"cep": cep})

		print("Informe seu cpf")
		cpf = input()
		informacoes.update({"cpf": cpf})

		print("Informe sua senha")
		senha = input()
		informacoes.update({"senha": senha})

		print("Informe codigo de banco")
		id_bancario = input()
		informacoes.update({"id_bancario": id_bancario})

		print("Informe codigo de agencia")
		agencia = input()
		informacoes.update({"codigo_agencia": agencia})

		print("Informe numero de conta")
		conta_corrente = input()
		informacoes.update({"conta_corrente": conta_corrente})

		return informacoes

	def menu_login(self):
		informacoes = {}

		print("Informe CPF")
		cpf = input()
		informacoes.update({"cpf": cpf})

		print("Informe senha")
		senha = input()
		informacoes.update({"senha": senha})

		return informacoes

	#def menu_autenticado(self):

