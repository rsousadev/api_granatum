#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""      
    Documento de integração Python API's

    CEP E CPF TEM QUE SER VALIDOS
    
"""

__author__ = "Ricardo Sousa"
__copyright__ = "Free"
__credits__ = "Ricardo De Maria Sousa"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ricardo Sousa"
__email__ = "ricardo.dmsousa@gmail.com"
__status__ = "Production"

import re
import sys
import time
from datetime import datetime
from granatum import granatum
from active_campaign import contacts
from e_notas import emitir_nfe
from memberkit import adiciona_um_aluno

"""Pega os valores enviados pelo PHP"""

nome = 'Ricardo Sousa'
cpf = '00000000000'
email_validar = 'ricardo.dmsousa@gmail.com'
rua = 'rua dos cafés'
numer = '111'
bairro = 'cafezeiro'
complemento = ''
cep = '111111111'
valor = '123'
qtd_repet = '0'

"""Seta os dados para padronizar o envio """

nome = re.sub(r"(\w)([A-Z])", r"\1 \2", nome)
rua = re.sub(r"(\w)([A-Z])", r"\1 \2", rua)
numer = re.sub(r"(\w)([A-Z])", r"\1 \2", numer)
bairro = re.sub(r"(\w)([A-Z])", r"\1 \2", bairro)
cidade = re.sub(r"(\w)([A-Z])", r"\1 \2", cidade)
uf = re.sub(r"(\w)([A-Z])", r"\1 \2", uf)
complemento = re.sub(r"(\w)([A-Z])", r"\1 \2", complemento)

"""Inserir Lançamento Granatum"""

now = datetime.now()
data = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
lanca_granatum = granatum.Granatum(nome, cpf, email_validar, rua, 
                                   numer, bairro, complemento, cep)

return_granatum = lanca_granatum.checkclient()
lanca_granatum.insert_sale(return_granatum,'Produto',
         'conta_id', 'categoria_id', valor,
        data,'forma_pagamento_id','cetro_custo_lucro', 'quantidade_repetições', data)


