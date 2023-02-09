import datetime

import Produtos
import Pessoal


# main esta sendo usada, no momento, para fazer testes nas classes criadas.

if __name__ == '__main__':

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