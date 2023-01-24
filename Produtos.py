import datetime


tam = 100


class TesouroDireto:
	def __init__(self):
		self.__nome = ""
		self.__data_vencimento = ""
		self.__indexador = ""
		self.__juros_mensal = 0
		self.__juros_anual = 0
		self.__valor = 0

	# Getters e setters de nome.

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome):
		if isinstance(nome, str) and len(nome) <= tam:
			self.__nome = nome
		elif not isinstance(nome, str):
			raise TypeError("Apenas string e aceita.")
		elif not len(nome) <= tam:
			raise Exception("Deve conter ate 80 caracteres.")

	# Getters e setters de data_vencimento.

	@property
	def data_vencimento(self):
		return self.__data_vencimento

	@data_vencimento.setter
	def data_vencimento(self, data_vencimento):
		if isinstance(data_vencimento, datetime.datetime):
			self.__data_vencimento = data_vencimento
		else:
			raise TypeError("Informe uma data.")

	# Getters e setters de indexador.

	@property
	def indexador(self):
		return self.__indexador

	@indexador.setter
	def indexador(self, indexador):
		if isinstance(indexador, str):
			if indexador == "IPCA" or indexador == "SELIC" or indexador == "IPG":
				self.__indexador = indexador
			else:
				raise Exception("Indexador deve ser: ICPA ou SELIC ou IPG.")
		else:
			raise TypeError("Apenas string e aceita.")

	# Getters e setters de juros_mensal.

	
	