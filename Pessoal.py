import datetime
import warnings

tam = 60
tam_cpf = 14
tam_identidade = 10
tam_casa_ou_apt = 1001
tam_cep = 8
tam_telefone = 14
tam_agencia = 6
tam_conta_corrente = 7

# Usuario

class Usuario:
	id_usuario = 0

	def __init__(self):
		Usuario.id_usuario += 1

		Usuario.lista_sexo = ["M", "F", "O"]
		Usuario.lista_estado_civil = ["solteiro", "namorando", "casado", "separado", "divorciado", "viuvo"]

		self.__id = Usuario.id_usuario
		self.__nome = ""		
		self.__cpf = ""			
		self.__identidade = ""	
		self.__filiacao = ""	
		self.__sexo = ""		
		self.__estado_civil = ""
		self.__naturalidade = ""
		self.__cidade = ""		
		self.__bairro = ""		
		self.__rua = ""			
		self.__casa_ou_apt = ""	
		self.__cep = ""			
		self.__uf = ""			
		self.__telefone = []	
		self.__email = ""		
		self.__pais = ""
		self.__escolaridade = ""
		self.__cargo = ""
		self.__id_bancario = ""
		self.__agencia = ""
		self.__conta_corrente = ""
		self.__senha = ""

		self.__data_nascimento = ""
		self.__renda_mensal = 0.0
		
	# Getter de id.
	@property
	def id(self):
		return self.__id

	# Getter e setter de nome.

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

	# Getter e setter de CPF.

	@property
	def cpf(self):
		return self.__cpf

	@cpf.setter
	def cpf(self, cpf):
		if isinstance(cpf, str):
			if len(cpf) == tam_cpf:
				self.__cpf = cpf
				return True
			else:
				warnings.warn("cpf deve conter 14 caracters.")
		else:
			warnings.warn("cpf aceita apenas tipo string.")

		return False

	# Getter e setter identidade

	@property
	def identidade(self):
		return self.__identidade

	@identidade.setter
	def identidade(self, identidade):
		if isinstance(identidade, str):
			if len(identidade) == tam_identidade:
				self.__identidade = identidade
				return True
			else:
				warnings.warn("identidade deve conter 10 caracters.")
		else:
			warnings.warn("identidade aceita apenas tipo string.")

		return False

	# Getter e setter filiacao

	@property
	def filiacao(self):
		return self.__filiacao

	@filiacao.setter
	def filiacao(self, filiacao):
		if isinstance(filiacao, str):
			if len(filiacao) == tam:
				self.__filiacao = filiacao
				return True
			else:
				warnings.warn("filiacao deve conter " + str(tam) + " caracters.")
		else:
			warnings.warn("filiacao aceita apenas tipo string.")

		return False

	# Getter e setter sexo

	@property
	def sexo(self):
		return self.__sexo

	@sexo.setter
	def sexo(self, sexo):
		if isinstance(sexo, str):
			if sexo in Usuario.lista_sexo:
				self.__sexo = sexo
				print("SIM")
				return True
			else:
				warnings.warn("sexo deve conter ser M, F ou O.")
		else:
			warnings.warn("sexo aceita apenas tipo string.")

		return False

	# Getter e setter estado_civil

	@property
	def estado_civil(self):
		return self.__estado_civil

	@estado_civil.setter
	def estado_civil(self, estado_civil):
		if isinstance(estado_civil, str):
			if estado_civil in Usuario.lista_estado_civil:
				self.__estado_civil = estado_civil
				return True
			else:
				warnings.warn("estado_civil deve conter 10 caracters.")
		else:
			warnings.warn("estado_civil aceita apenas tipo string.")

		return False		
	
	# Getter e setter de naturalidade.

	@property
	def naturalidade(self):
		return self.__naturalidade

	@naturalidade.setter
	def naturalidade(self, naturalidade):
		if isinstance(naturalidade, str):
			if len(naturalidade) <= tam:
				self.__naturalidade = naturalidade
				return True
			else:
				warnings.warn("naturalidade deve conter ate 100 caracteres.")
		else:
			warnings.warn("naturalidade aceita apenas tipo string.")

		return False

	# Getter e setter de cidade.

	@property
	def cidade(self):
		return self.__cidade

	@cidade.setter
	def cidade(self, cidade):
		if isinstance(cidade, str):
			if len(cidade) <= tam:
				self.__cidade = cidade
				return True
			else:
				warnings.warn("cidade deve conter ate 100 caracteres.")
		else:
			warnings.warn("cidade aceita apenas tipo string.")

		return False

	# Getter e setter de bairro.

	@property
	def bairro(self):
		return self.__bairro

	@bairro.setter
	def bairro(self, bairro):
		if isinstance(bairro, str):
			if len(bairro) <= tam:
				self.__bairro = bairro
				return True
			else:
				warnings.warn("bairro deve conter ate 100 caracteres.")
		else:
			warnings.warn("bairro aceita apenas tipo string.")

		return False

	# Getter e setter de rua.

	@property
	def rua(self):
		return self.__rua

	@rua.setter
	def rua(self, rua):
		if isinstance(rua, str):
			if len(rua) <= tam:
				self.__rua = rua
				return True
			else:
				warnings.warn("rua deve conter ate 100 caracteres.")
		else:
			warnings.warn("rua aceita apenas tipo string.")

		return False

	# Getter e setter de casa_ou_apt.

	@property
	def casa_ou_apt(self):
		return self.__casa_ou_apt

	@casa_ou_apt.setter
	def casa_ou_apt(self, casa_ou_apt):
		if isinstance(casa_ou_apt, int):
			if casa_ou_apt in range(1, tam_casa_ou_apt):
				self.__casa_ou_apt = casa_ou_apt
				return True
			else:
				warnings.warn("casa_ou_apt deve ser entre 1 e 1000.")
		else:
			warnings.warn("casa_ou_apt aceita apenas tipo int.")

		return False


	# Getter e setter de cep.

	@property
	def cep(self):
		return self.__cep

	@cep.setter
	def cep(self, cep):
		if isinstance(cep, str):
			if len(cep) == tam_cep:
				self.__cep = cep
				return True
			else:
				warnings.warn("cep ser ter " + tam_cep + " caracteres.")
		else:
			warnings.warn("cep aceita apenas tipo string.")

		return False

	# Getter e setter de uf.

	@property
	def uf(self):
		return self.__uf

	@uf.setter
	def uf(self, uf):
		if isinstance(uf, str):
			if len(uf) == tam:
				self.__uf = uf
				return True
			else:
				warnings.warn("uf ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("uf aceita apenas tipo string.")

		return False

	# Getter e setter de telefone.

	@property
	def telefone(self):
		return self.__telefone

	@telefone.setter
	def telefone(self, telefone):
		if isinstance(telefone, str):
			if len(telefone) == tam_telefone:
				self.__telefone.append(telefone)
				return True
			else:
				warnings.warn("telefone ser ter ate " + tam_telefone + " caracteres.")
		else:
			warnings.warn("telefone aceita apenas tipo string.")

		return False

	# Getter e setter de email.

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, email):
		if isinstance(email, str):
			if len(email) == tam:
				self.__email = email
				return True
			else:
				warnings.warn("email ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("email aceita apenas tipo string.")

		return False

	# Getter e setter de pais.

	@property
	def pais(self):
		return self.__pais

	@pais.setter
	def pais(self, pais):
		if isinstance(pais, str):
			if len(pais) == tam:
				self.__pais = pais
				return True
			else:
				warnings.warn("pais ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("pais aceita apenas tipo string.")

		return False

	# Getter e setter de escolaridade.

	@property
	def escolaridade(self):
		return self.__escolaridade

	@escolaridade.setter
	def escolaridade(self, escolaridade):
		if isinstance(escolaridade, str):
			if len(escolaridade) == tam:
				self.__escolaridade = escolaridade
				return True
			else:
				warnings.warn("escolaridade ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("escolaridade aceita apenas tipo string.")

		return False

	# Getter e setter de cargo.

	@property
	def cargo(self):
		return self.__cargo

	@cargo.setter
	def cargo(self, cargo):
		if isinstance(cargo, str):
			if len(cargo) == tam:
				self.__cargo = cargo
				return True
			else:
				warnings.warn("cargo ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("cargo aceita apenas tipo string.")

		return False

	# Getter e setter de id_bancario.

	@property
	def id_bancario(self):
		return self.__id_bancario

	@id_bancario.setter
	def id_bancario(self, id_bancario):
		if isinstance(id_bancario, int):
			if id_bancario in range(0, 1000):
				self.__id_bancario = id_bancario
				return True
			else:
				warnings.warn("id_bancario deve ser entre 0 e 999.")
		else:
			warnings.warn("id_bancario aceita apenas tipo int.")
		return False

	# Getter e setter de agencia.

	@property
	def agencia(self):
		return self.__agencia

	@agencia.setter
	def agencia(self, agencia):
		if isinstance(agencia, str):
			if len(agencia) == tam:
				self.__agencia = agencia
				return True
			else:
				warnings.warn("agencia ser ter ate " + tam_agencia + " caracteres.")
		else:
			warnings.warn("agencia aceita apenas tipo string.")

		return False

	# Getter e setter de conta_corrente.

	@property
	def conta_corrente(self):
		return self.__conta_corrente

	@conta_corrente.setter
	def conta_corrente(self, conta_corrente):
		if isinstance(conta_corrente, str):
			if len(conta_corrente) == tam:
				self.__conta_corrente = conta_corrente
				return True
			else:
				warnings.warn("conta_corrente ser ter ate " + tam_conta_corrente + " caracteres.")
		else:
			warnings.warn("conta_corrente aceita apenas tipo string.")

		return False
	
	# Getter e setter de senha.

	@property
	def senha(self):
		return self.__senha

	@senha.setter
	def senha(self, senha):
		if isinstance(senha, str):
			if len(senha) == tam:
				self.__senha = senha
				return True
			else:
				warnings.warn("senha ser ter ate " + tam + " caracteres.")
		else:
			warnings.warn("senha aceita apenas tipo string.")

		return False

	# Getter e setter de renda_mensal.

	@property
	def renda_mensal(self):
		return self.__renda_mensal

	@renda_mensal.setter
	def renda_mensal(self, renda_mensal):
		if isinstance(renda_mensal, float):
			if renda_mensal >= 0:
				self.__renda_mensal = renda_mensal
				return True
			else:
				warnings.warn("renda_mensal deve ser maior igual a 0.")
		else:
			warnings.warn("renda_mensal aceita apenas tipo float.")
		return False
