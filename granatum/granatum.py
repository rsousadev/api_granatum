#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""      
    Documento de integração Python Granatum API
    
    Cadastra um cliente se ele não existir e realiza um lançamento em uma conta especifica

    #construtor 

    seta o cadastro do cliente e as confiruações de url

    #checkClient

    checa se o cliente existe, caso o cliente exista pega o dia, se não ele cadastra o cliente e pega o id
    
    #insert_sale

    insere uma venda para o cliente selecionado

    #use sem moderação!
"""
 
__author__ = "Ricardo Sousa"
__copyright__ = "Free"
__credits__ = "Ricardo De Maria Sousa"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ricardo Sousa"
__email__ = "ricardo.dmsousa@gmail.com"
__status__ = "Production"


import urllib.parse
import json
import urllib.request
import requests
import time
from datetime import datetime

class Granatum:
    
    """ seta os dados do cliente e urls de envio de dados """
    
    def __init__(self, nome, documento, email, telefone, endereco, endereco_numero, bairro, endereco_complemento, cep):
        self.data = {'nome':nome,'documento':documento,'email':email,'telefone':telefone, 'endereco':endereco, 'endereco_numero':endereco_numero, 'bairro':bairro, 'endereco_complemento':endereco_complemento, 'cep':cep}
        url = 'https://api.granatum.com.br/v1/clientes'
        self.header = '?access_token='
        self.cliente = 'https://api.granatum.com.br/v1/clientes'
        self.response = requests.get(url + self.header)
        self.response_json = self.response.json()
        self.url_lanc = 'https://api.granatum.com.br/v1/lancamentos'

    """Verifica se o cliente existe se não existir ele cria um cliente"""
    
    def checkclient(self):
        if self.response.status_code == 200:
            inserir_cliente = requests.post(self.cliente + self.header, json=self.data)
            return_status = inserir_cliente.json()
            print(return_status)
            if inserir_cliente.status_code != 201:
                status_erro = str(return_status['errors']['documento'][0])
                if status_erro == 'O CPF/CNPJ deste cliente/fornecedor já está sendo utilizado por outro cliente/fornecedor cadastrado.':
                    cont_list = len(self.response_json)
                    try:
                        for i in range(cont_list):
                            if str(self.response_json[i]['documento']) == str(self.data['documento']):
                                client_doc_id = self.response_json[i]['id']                                
                                i += 1
                    except IndexError:
                        pass
                    return_code = 'ERRO AO INSERIR USUÁRIO'
                    write_in_doc = '\n' + '*' * 10 + str(return_code) + '*' * 10 + '\n' +  'ERRO: ' + str(return_status)
                    arq = open('log_de_erro.txt', 'w')
                    arq.write(write_in_doc)
                    arq.close()
            else:
                client_doc_id = return_status['id']
        return client_doc_id

    """Lança uma venda para o cliente criado/selecionado dentro de uma conta especifica"""

    def insert_sale(self, client_doc_id, descricao, conta_id, categoria_id, valor, data_vencimento,
            forma_pagamento, centro_custo_lucro_id, total_repeticoes, data_competencia):
        data = {'pessoa_id':client_doc_id, 'descricao':descricao, 'conta_id':conta_id,
                'categoria_id':categoria_id,'valor':valor, 'data_vencimento':data_vencimento,
                'forma_pagamento_id':forma_pagamento,'centro_custo_lucro_id':centro_custo_lucro_id,
                'total_repeticoes':total_repeticoes,'pagamento_automatico':'FALSE',
                'observacao':'Pagamento Rede','data_competencia':data_competencia}
        lanc = requests.post(self.url_lanc + self.header, json=data)
        print(lanc.json())

