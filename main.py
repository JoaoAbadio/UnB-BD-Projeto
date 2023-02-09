import datetime

import Produtos
import Pessoal
import Apresentacao
import Controladora


# main esta sendo usada, no momento, para fazer testes nas classes criadas.

if __name__ == '__main__':

	apresentacao = Apresentacao.Apresentacao()
	controladora = Controladora.Controladora()

	saida = False

	while not saida:
		opcao_inicial = apresentacao.menu_inicial()

		if opcao_inicial == 1:
			opcao_produtos = apresentacao.menu_produtos()
			controladora.produtos(opcao_produtos)
			continue

		elif opcao_inicial == 2:
			informacoes = apresentacao.menu_cadastrar()
			print(informacoes)
			usuario = Pessoal.Usuario()
			usuario.cadastrar(informacoes)

			controladora.adicionar_usario(usuario)

		elif opcao_inicial == 4:
			saida = True

	u1 = Pessoal.Usuario()
	u1.sexo = "M"
	print(u1.sexo)


	"""
		Data

		import datetime

		x = datetime.datetime(2018, 6, 1)

		print(x.strftime("%x"))
		print(teste.strftime("%X"))
	"""