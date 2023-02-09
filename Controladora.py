import mysql.connector

import Produtos
import Pessoal
import Apresentacao



class Controladora:
	def __init__(self):
		self.__mydb = mysql.connector.connect(
		  host="localhost",
		  user="unb",
		  password="180123394",
		  database="investimentos"
		)

		self.__mycursor = self.__mydb.cursor()


	def produtos(self, opcao):
		if opcao == 1:
			self.__mycursor.execute("SELECT * FROM tesouro_direto")
			resultado = self.__mycursor.fetchall()

			for produto in resultado:
				print(resultado)

		elif opcao == 2:
			self.__mycursor.execute("SELECT * FROM fundo_investimento")
			resultado = self.__mycursor.fetchall()

			for produto in resultado:
				print(resultado)

		elif opcao == 3:
			self.__mycursor.execute("SELECT * FROM renda_fixa_variavel")
			resultado = self.__mycursor.fetchall()

			for produto in resultado:
				print(resultado)

	def adicionar_usario(self, usuario):
		sql = "INSERT INTO usuario (nome, cpf, identidade, filiacao, sexo, estado_civil, naturalidade,"\
		+ " cidade, bairro, rua, numero, cep, uf, email, pais, escolaridade, cargo, data_nascimento,"\
		+ " renda_mensal, senha, id_bancario, codigo_agencia, conta_corrente)"\
		+ " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		
		val = (usuario.nome, usuario.cpf, usuario.identidade, usuario.filiacao, usuario.sexo,
			usuario.estado_civil, usuario.naturalidade, usuario.cidade, usuario.bairro,
			usuario.rua, usuario.numero, usuario.cep, usuario.uf, usuario.email, usuario.pais,
			usuario.escolaridade, usuario.cargo, usuario.data_nascimento,
			usuario.renda_mensal,  usuario.senha, usuario.id_bancario,
			usuario.codigo_agencia, usuario.conta_corrente)
		
		self.__mycursor.execute(sql, val)
		self.__mydb.commit()
		print(self.__mycursor.rowcount, "record inserted.")
