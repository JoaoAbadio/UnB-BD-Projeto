import datetime

import Produtos


if __name__ == '__main__':

	teste = Produtos.RendaFixaVariavel()

	teste.valor_minimo = 150.0
	print(teste.valor_minimo)

	"""
		Data

		import datetime

		x = datetime.datetime(2018, 6, 1)

		print(x.strftime("%x"))
		print(teste.strftime("%X"))
	"""