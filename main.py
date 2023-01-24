import datetime

import Produtos


if __name__ == '__main__':
	tesouro_direto = Produtos.TesouroDireto()
	
	tesouro_direto.indexador = 2
	print(tesouro_direto.indexador)

	"""
		Data

		import datetime

		x = datetime.datetime(2018, 6, 1)

		print(x.strftime("%x"))
	"""