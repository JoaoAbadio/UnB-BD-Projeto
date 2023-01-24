import datetime
import warnings

import Auxiliar

tam = 100


# Tesoudo Direto.

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
		if isinstance(nome, str):
			if len(nome) <= tam:
				self.__nome = nome
				return True
			else:
				warnings.warn("nome deve conter ate 100 caracteres.")
		else:
			warnings.warn("nome aceita apenas tipo string.")

		return False

	# Getters e setters de data_vencimento.

	@property
	def data_vencimento(self):
		return self.__data_vencimento

	@data_vencimento.setter
	def data_vencimento(self, data_vencimento):
		if isinstance(data_vencimento, datetime.datetime):
			self.__data_vencimento = data_vencimento
			return True
		else:
			warnings.warn("data_vencimento aceita apenas tipo data.")

		return False

	# Getters e setters de indexador.

	@property
	def indexador(self):
		return self.__indexador

	@indexador.setter
	def indexador(self, indexador):
		if isinstance(indexador, str):
			if indexador == "IPCA" or indexador == "SELIC" or indexador == "IPG":
				self.__indexador = indexador
				return True
			else:
				warnings.warn("indexador deve ser: ICPA ou SELIC ou IPG.")
		else:
			warnings.warn("indexador aceita apenas tipo string.")

		return False

	# Getters e setters de juros_mensal.

	@property
	def juros_mensal(self):
		return self.__juros_mensal

	@juros_mensal.setter
	def juros_mensal(self, juros_mensal):
		if isinstance(juros_mensal, float):
			if juros_mensal >= 0:
				self.__juros_mensal = juros_mensal
				return True
			else:
				warnings.warn("juros_mensal deve ser maior ou igual a 0.")
		else:
			warnings.warn("juros_mensal aceita apenas tipo float.")

		return False

	# Getters e setters de juros_anual.

	@property
	def juros_anual(self):
		return self.__juros_anual

	@juros_anual.setter
	def juros_anual(self, juros_anual):
		if isinstance(juros_anual, float):
			if juros_anual >= 0:
				self.__juros_anual = juros_anual
				return True
			else:
				warnings.warn("juros_anual deve ser maior ou igual a 0.")
		else:
			warnings.warn("juros_anual aceita apenas tipo float.")

		return False

	# Getters e setters de valor.

	@property
	def valor(self):
		return self.__valor

	@valor.setter
	def valor(self, valor):
		if isinstance(valor, float):
			if valor >= 0:
				self.__valor = valor
				return True
			else:
				warnings.warn("valor deve ser maior ou igual a 0.")
		else:
			warnings.warn("valor aceita apenas tipo float.")

		return False


# Fundo de Investimento

class FundoInvestimento:
	def __init__(self):
		self.__classe = ""
		self.__prazo_resgate = 0
		self.__nome = ""
		self.__valor_minimo = 0
		self.__data_resgate = 0

	# Getters e setters de classe.

	@property
	def classe(self):
		return self.__classe

	@classe.setter
	def classe(self, classe):
		if isinstance(classe, str):
			if classe == "acao" or classe == "multimercado" or classe == "renda fixa":
				self.__classe = classe
				return True
			else:
				warnings.warn("classe deve ser: acao ou multimercado ou renda fixa.")
		else:
			warnings.warn("classe deve ser string.")

		return False
	
	# Getters e setters de prazo_resgate.

	@property
	def prazo_resgate(self):
		return self.__prazo_resgate

	@prazo_resgate.setter
	def prazo_resgate(self, prazo_resgate):
		if isinstance(prazo_resgate, int):
			if prazo_resgate == 6 or prazo_resgate == 12 or prazo_resgate == 24	\
			   or prazo_resgate == 36 or prazo_resgate == 48 or prazo_resgate == 60:
				self.__prazo_resgate = prazo_resgate
				return True
			else:
				warnings.warn("prazo_resgate deve ser: 6, 12, 24, 36, 48 ou 60.")
		else:
			warnings.warn("prazo_resgate deve ser float.")

	# Getters e setters de nome.

	@property
	def nome(self):
		return self.__nome
	
	@nome.setter
	def nome(self, nome):
		if isinstance(nome, str):
			if len(nome) <= tam:
				self.__nome = nome
				return True
			else:
				warnings.warn("nome deve conter ate 100 caracteres.")
		else:
			warnings.warn("nome deve ser string.")

		return False

	# Getters e setters de valor_minimo.

	@property
	def valor_minimo(self):
		return self.__valor_minimo

	@valor_minimo.setter
	def valor_minimo(self, valor_minimo):
		if isinstance(valor_minimo, float):
			if valor_minimo >= 0:
				self.__valor_minimo = valor_minimo
				return True
			else:
				warnings.warn("valor_minimo deve ser maior ou igual a zero.")
		else:
			warnings.warn("valor_minimo deve ser float")

		return False

	# Getters e setters de data_resgate.

	@property
	def data_resgate(self):
		return self._data_resgate

	@data_resgate.setter
	def data_resgate(self, data_resgate):
		if isinstance(data_resgate, datetime.datetime):
			self.__data_resgate = data_resgate
			return True
		else:
			warnings.warn("data_resgate aceita apenas tipo data.")
	
		return False


	