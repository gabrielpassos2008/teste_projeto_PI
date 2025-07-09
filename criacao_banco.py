import sqlite3
from datetime import datetime
def criar_banco():
    conexao = sqlite3.connect('banco_chegando_pi.db')
    criar_tab_usuario_adm(conexao)
    criar_tab_empresa_guincho(conexao)
    criar_tab_seguradora(conexao)
    criar_tab_solicitacao_de_guincho(conexao)
#criação de tabela usuario_adm
def criar_tab_usuario_adm(conn):
    cursor = conn.cursor()
    cursor.execute('''
     CREATE TABLE IF NOT EXISTS usuario_adm (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        senha TEXT NOT NULL,
        email TEXT NOT NULL,
        tipo INTEGER NOT NULL
    );
    ''')

#criação de tabela empresa_guincho
def criar_tab_empresa_guincho(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresa_guincho(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        id_usuario_aprovador INTEGER ,
        status_aprovacao BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY (id_usuario_aprovador) REFERENCES usuario_adm(id)            
    );
    ''')
#criação de tabela seguradora
def criar_tab_seguradora(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seguradora(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT  NULL,
        id_usuario_aprovacao INTEGER,
        status_aprovacao BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY (id_usuario_aprovacao) REFERENCES usuario_adm(id)
    );
    ''')
#criação de tabela solicitacao_de_guincho
def criar_tab_solicitacao_de_guincho(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS solicitacao_de_guincho(
        id  INTEGER PRIMARY KEY  AUTOINCREMENT,
        placa_carro TEXT NOT NULL,               
        local_de_origem TEXT NOT NULL,
        local_de_destino TEXT NOT NULL,           
        status INT DEFAULT 0,
        data_hora DATETIME,
        id_seguradora INTEGER ,
        id_guincho INTEGER ,
        FOREIGN KEY(id_seguradora) REFERENCES seguradora(id),
        FOREIGN KEY(id_guincho) REFERENCES empresa_guincho(id)                   
    );
    ''')

