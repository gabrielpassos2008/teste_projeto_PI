import sqlite3
from datetime import datetime

class Usuario():
    def __init__(self):
        self.id = id
        self.logado = False

usuario = Usuario()

def adicionar_usuario_adm(senha,email,tipo):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO usuario_adm (senha,email,tipo)
    VALUES(?,?,?)
    ''',(senha,email,tipo))
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_seguradora(nome,email,senha):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO seguradora (nome,email,senha)
    VALUES(?,?,?)
    ''',(nome,email,senha))
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_empresa_de_guincho(nome,email,senha):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO empresa_guincho (nome,email,senha)
    VALUES(?,?,?)
    ''',(nome,email,senha))
    conexao.commit()
    cursor.close()
    conexao.close()

def inserir_solicitacao_de_guincho(placa_carro, local_de_origem, local_de_destino,status, data_hora,id_guincho):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO solicitacao_de_guincho(placa_carro,local_de_origem,local_de_destino,status,data_hora,id_guincho)
    VALUES(?,?,?,?,?,?)
    ''',(placa_carro,local_de_origem,local_de_destino,status,data_hora,id_guincho))
    resultado = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if resultado > 0:
        print('achou')
        return True
    else:
        print('nao achou')
        return False

def autorizar_seguradora(id_aprovador,status, id_empresa):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    UPDATE seguradora
    SET id_usuario_aprovacao = ?, status_aprovacao = ?
    WHERE id = ?
    ''', (id_aprovador,status, id_empresa))
    resultado = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if resultado > 0:
        print('achou')
        return True
    else:
        print('nao achou')
        return False
    
def autorizar_empresa_guincho(id_aprovador,status, id_guincho):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    UPDATE empresa_guincho
    SET id_usuario_aprovador = ?, status_aprovacao = ?
    WHERE id = ?
    ''', (id_aprovador,status, id_guincho))
    resultado = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if resultado > 0:
        print('achou')
        return True
    else:
        print('nao achou')
        return False
    
def login_empresa_de_guincho(email,senha):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT id, nome FROM empresa_guincho
    WHERE email = ? AND senha = ? AND status_aprovacao = 1 
    ''',(email,senha))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    if resultado:
        usuario.id = resultado[0]
        usuario.logado = True
        print('achou')
        return usuario.logado
    else:
        print('nao achou')
        return usuario.logado

def login_seguradora(email,senha):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT id, nome FROM seguradora
    WHERE email = ? AND senha = ? AND status_aprovacao = 1 
    ''',(email,senha))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    if resultado:
        print('achou')
        usuario.id = resultado[0]
        usuario.logado = True
        return usuario.logado
    else:
        print('nao achou')
        return usuario.logado

def login_usuario_adm(email,senha):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT id, email,senha FROM usuario_adm
    WHERE email = ? AND senha = ?
    ''',(email,senha)) 
    resultado = cursor.fetchone()    
    cursor.close()
    conexao.close()
    if resultado:
        print('achou')        
        usuario.id = resultado[0]
        usuario.logado = True
        return usuario.logado
    else:
        print('nao achou')
        return usuario.logado

def buscar_solicitacoes_guincho():
    id = usuario.id
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT id, placa_carro, local_de_origem, local_de_destino,status
    FROM solicitacao_de_guincho
    WHERE status = 0 AND id_guincho = ?
    ''',(id,))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def buscar_empresa_guincho():
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT id,nome
    FROM empresa_guincho
    WHERE status_aprovacao = 1
    ''')
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def aceitar_pedido(status,id):
    conexao = sqlite3.connect('banco_chegando_pi.db')
    cursor = conexao.cursor()
    cursor.execute('''
    UPDATE solicitacao_de_guincho
    SET status = ?
    WHERE id = ?
    ''', (status,id))
    resultado = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if resultado > 0:
        print('achou')
        return True
    else:
        print('nao achou')
        return False

# login_empresa_de_guincho( 'rapido@guincho.com', 'rapido456')
# login_seguradora('suporte@segurototal.com', 'seg003')
def inserts_completo():
    adicionar_usuario_adm('senha123', 'admin1@empresa.com', 1)
    adicionar_usuario_adm('senha456', 'admin2@empresa.com', 1)
    adicionar_usuario_adm('senha789', 'admin3@empresa.com', 2)
    adicionar_seguradora('Protege Bem', 'contato@protegebem.com', 'seg001'),
    adicionar_seguradora('Vida Segura', 'atendimento@vidasegura.com', 'seg002'),
    adicionar_seguradora('Seguro Total', 'suporte@segurototal.com', 'seg003')
    adicionar_empresa_de_guincho('Guincho Express', 'express@guincho.com', 'exp123')
    adicionar_empresa_de_guincho('Resgate Rápido', 'rapido@guincho.com', 'rapido456')
    adicionar_empresa_de_guincho('Super Socorro', 'super@socorro.com', 'super789')
    inserir_solicitacao_de_guincho('AAA1B23', 'Rua Alfa, 100', 'Av. Central, 300', '0', datetime.now(),1)
    inserir_solicitacao_de_guincho('BBB2C34', 'Rua Beta, 200', 'Av. Norte, 400', '0', datetime.now(),1) 
    inserir_solicitacao_de_guincho('CCC3D45', 'Rua Gama, 300', 'Av. Sul, 500', '0', datetime.now(),1)
    autorizar_empresa_guincho(1,1,1)
    autorizar_seguradora(2,1,3)
