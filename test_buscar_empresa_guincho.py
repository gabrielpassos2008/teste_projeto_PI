import sqlite3
import pytest
import funcoes_banco as model
import criacao_banco as banco

@pytest.fixture
def conexao():
    # Cria um banco em memória para testes
    conn = sqlite3.connect(':memory:')
    banco.criar_tab_empresa_guincho(conn)
    yield conn
    conn.close()

def test_buscar_empresa_guincho(conexao):
    model.adicionar_usuario_adm('1234','1234@gmail.com',1)
    model.adicionar_empresa_de_guincho(conexao,'Guincho Express', 'express@guincho.com', 'exp123')
    model.adicionar_empresa_de_guincho(conexao,'Resgate Rápido', 'rapido@guincho.com', 'rapido456')
    model.autorizar_empresa_guincho(conexao,1,1,1)
    model.autorizar_empresa_guincho(conexao,1,1,2)
    usuarios = model.buscar_empresa_guincho(conexao)
    assert (1,'Guincho Express') in usuarios
    assert (2,'Resgate Rápido') in usuarios
    assert len(usuarios) == 2

def test_autorizar_empresa_guincho(conexao):
    model.adicionar_usuario_adm('1234','1234@gmail.com',1)
    model.adicionar_empresa_de_guincho(conexao,'Guincho Express', 'express@guincho.com', 'exp123')
    assert model.autorizar_empresa_guincho(conexao,1,1,1) == True
    assert model.autorizar_empresa_guincho(conexao,1,1,4) == False



