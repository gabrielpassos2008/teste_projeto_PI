import tkinter as tk 
from tkinter import messagebox
import funcoes_banco as model
from datetime import datetime

valor_padx = 10
valor_pady = 10


def abrir_j_selecionar_login():
    janela = tk.Toplevel()
    janela.title('selecione qual login deseja fazer')

    label = tk.Label(janela,text='selecione qual login deseja fazer')
    label.grid(row=0,column=0,padx=valor_padx,pady=valor_pady)

    botao_login_adm = tk.Button(janela,text='Login usuario ADM',command=abrir_j_login_usuario_adm)
    botao_login_adm.grid(row=1,column=0,padx=valor_padx,pady=valor_pady)

    botao_login_empresa_guincho = tk.Button(janela,text='Login empresa de guincho',command=abrir_j_login_empresa_guincho)
    botao_login_empresa_guincho.grid(row=2,column=0,padx=valor_padx,pady=valor_pady)

    botao_login_seguradora = tk.Button(janela,text='Login seguradora',command=abrir_j_login_seguradora)
    botao_login_seguradora.grid(row=3,column=0,padx=valor_padx,pady=valor_pady)

def abrir_j_login_seguradora():

    j_login = tk.Toplevel()
    j_login.title("Login seguradora")
    j_login.geometry("300x260+800+400")

    label_text = tk.Label(j_login,text='Informe os dados de login')
    label_text.grid(row=0,column=1,padx=20,pady=20)

    label_email = tk.Label(j_login,text='Email:')
    label_email.grid(row=1,column=0,padx=20,pady=20)
    entry_email = tk.Entry(j_login)
    entry_email.grid(row=1,column=1,padx=5,pady=5)

    label_senha = tk.Label(j_login,text='Senha:') 
    label_senha.grid(row=2,column=0,padx=20,pady=20)
    entry_senha = tk.Entry(j_login)
    entry_senha.grid(row=2,column=1,padx=20,pady=20)

    def tentar_login():
        email = entry_email.get()
        senha = entry_senha.get()
        if model.login_seguradora(email, senha):
            messagebox.showinfo("Login bem-sucedido", "Você entrou com sucesso!")
            abrir_j_principal_solicitar_guincho()
        else:
            messagebox.showerror("Erro de login", "Email ou senha incorretos.")
        model.login_seguradora(email,senha)
    
    botao_entrar = tk.Button(j_login,text='Entrar',command=tentar_login)
    botao_entrar.grid(row=3,column=1,padx=20,pady=20)

def abrir_j_login_empresa_guincho():
    
    j_login = tk.Toplevel()
    j_login.title("Login Empresa de guincho")
    j_login.geometry("300x260+200+200")
    
    label_text = tk.Label(j_login,text='Informe os dados de login')
    label_text.grid(row=0,column=1,padx=20,pady=20)

    label_email = tk.Label(j_login,text='Email:')
    label_email.grid(row=1,column=0,padx=20,pady=20)
    entry_email = tk.Entry(j_login)
    entry_email.grid(row=1,column=1,padx=5,pady=5)

    label_senha = tk.Label(j_login,text='Senha:') 
    label_senha.grid(row=2,column=0,padx=20,pady=20)
    entry_senha = tk.Entry(j_login)
    entry_senha.grid(row=2,column=1,padx=20,pady=20)

    def tentar_login():
        email = entry_email.get()
        senha = entry_senha.get()
        if model.login_empresa_de_guincho(email, senha):
            messagebox.showinfo("Login bem-sucedido", "Você entrou com sucesso!")
            abrir_j_princilpal_guincho()

        else:
            messagebox.showerror("Erro de login", "Email ou senha incorretos.")
        model.login_empresa_de_guincho(email,senha)
    
    botao_entrar = tk.Button(j_login,text='Entrar',command=tentar_login)
    botao_entrar.grid(row=3,column=1,padx=20,pady=20)

def abrir_j_login_usuario_adm():
    j_login = tk.Toplevel()
    j_login.title("Login Usuario adm")
    j_login.geometry("300x260+200+200")

    label_text = tk.Label(j_login,text='Informe os dados de login')
    label_text.grid(row=0,column=1,padx=20,pady=20)

    label_email = tk.Label(j_login,text='Email:')
    label_email.grid(row=1,column=0,padx=20,pady=20)
    entry_email = tk.Entry(j_login)
    entry_email.grid(row=1,column=1,padx=5,pady=5)

    label_senha = tk.Label(j_login,text='Senha:') 
    label_senha.grid(row=2,column=0,padx=20,pady=20)
    entry_senha = tk.Entry(j_login)
    entry_senha.grid(row=2,column=1,padx=20,pady=20)

    def tentar_login():
        email = entry_email.get()
        senha = entry_senha.get()
        if model.login_usuario_adm(email, senha):
            messagebox.showinfo("Login bem-sucedido", "Você entrou com sucesso!")
            abrir_j_principal_usuario_adm()
        else:
            messagebox.showerror("Erro de login", "Email ou senha incorretos.")
                
 
    botao_entrar = tk.Button(j_login,text='Entrar',command=tentar_login)
    botao_entrar.grid(row=3,column=1,padx=20,pady=20)

def abrir_j_principal_usuario_adm():
    #adiconar nova entry para informar o status
    j_principal = tk.Toplevel()
    j_principal.title('Janela principal')
    j_principal.geometry("400x360+200+200")

    var_guincho = tk.BooleanVar()
    var_seguradora = tk.BooleanVar()

    label_text_principal = tk.Label(j_principal,text='Informe os dados')
    label_text_principal.grid(row=0,column=0,padx=10,pady=20)

    label_id_aprovador = tk.Label(j_principal,text='Informe seu id:')
    label_id_aprovador.grid(row=1,column=0,padx=10,pady=20)
    entry_id_aprovador = tk.Entry(j_principal)
    entry_id_aprovador.grid(row=1,column=1,padx=10,pady=20)

    label_id_tabela = tk.Label(j_principal,text='Informe o id da empresa:')
    label_id_tabela.grid(row=2,column=0,padx=10,pady=20)
    entry_id_tabela = tk.Entry(j_principal)
    entry_id_tabela.grid(row=2,column=1,padx=10,pady=20)
    
    def criar_messagebox():
        if model.autorizar_empresa_guincho(entry_id_aprovador.get(),'1',entry_id_tabela.get()) or model.autorizar_seguradora(entry_id_aprovador.get(),'1',entry_id_tabela.get()):
            messagebox.showinfo("aviso", "Editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao autorizar")

    def atualizar_checkbuttons(origem):
        if origem == 'seguradora' and var_seguradora.get():
            var_guincho.set(False)
        elif origem == 'guincho' and var_guincho.get():
            var_seguradora.set(False)

    def autorizar():
        if var_guincho.get() == True and var_seguradora.get() == False:
            model.autorizar_empresa_guincho(entry_id_aprovador.get(),'1',entry_id_tabela.get())
            criar_messagebox()
        elif var_seguradora.get() == True and var_guincho.get() == False:
            model.autorizar_seguradora(entry_id_aprovador.get(),'1',entry_id_tabela.get())
            criar_messagebox()
        else:
            messagebox.showerror('Erro','informe os dados.')

    def cancelar():
        if var_guincho.get() == True and var_seguradora.get() == False:
            model.autorizar_empresa_guincho(entry_id_aprovador.get(),'0',entry_id_tabela.get())
            criar_messagebox()
        elif var_seguradora.get() == True and var_guincho.get() == False:
            model.autorizar_seguradora(entry_id_aprovador.get(),'0',entry_id_tabela.get())
            criar_messagebox()
        else:
            messagebox.showerror('Erro','informe os dados.')

    cb_seguradora = tk.Checkbutton(j_principal, variable=var_seguradora, text="Seguradora",command=lambda:atualizar_checkbuttons('seguradora'))
    cb_seguradora.grid(row=3, column=0, padx=10, pady=10)

    cb_guincho = tk.Checkbutton(j_principal, variable=var_guincho, text="Empresa de guincho",command=lambda:atualizar_checkbuttons('guincho'))
    cb_guincho.grid(row=3, column=1, padx=10, pady=10)

    botao_entrar = tk.Button(j_principal,text='Ativar',command=autorizar)
    botao_entrar.grid(row=4,column=0,padx=10,pady=20)

    botao_entrar = tk.Button(j_principal,text='Desativar',command=cancelar)
    botao_entrar.grid(row=4,column=1,padx=10,pady=20)

def abrir_j_principal_solicitar_guincho():
 
        j_principal = tk.Toplevel()
        j_principal.title('Solicitar guincho')
        j_principal.geometry('400x500+200+300')

        tk.Label(j_principal, text='Informe as informações solicitadas').grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(j_principal, text='Placa do carro').grid(row=1, column=0, padx=10, pady=5)
        entry_placa_carro = tk.Entry(j_principal)
        entry_placa_carro.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(j_principal, text='Local de origem').grid(row=2, column=0, padx=10, pady=5)
        entry_local_de_origem = tk.Entry(j_principal)
        entry_local_de_origem.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(j_principal, text='Local de destino').grid(row=3, column=0, padx=10, pady=5)
        entry_local_de_destino = tk.Entry(j_principal)
        entry_local_de_destino.grid(row=3, column=1, padx=10, pady=5)

        label_guincho = tk.Label(j_principal, text='Selecione um guincho:')
        label_guincho.grid(row=4, column=0, columnspan=2, pady=10)

        guinchos = model.buscar_empresa_guincho()

        row_guincho = 5

        def selecionar_guincho(id_guincho):
            global guincho_selecionado_id
            guincho_selecionado_id = id_guincho
            label_guincho_selecionado.config(text=f"Guincho selecionado: ID {id_guincho}")
        def inserir():
            placa_carro = entry_placa_carro.get()
            local_de_origem = entry_local_de_origem.get()
            local_de_destino = entry_local_de_destino.get()
            data = datetime.now()
            
            if guincho_selecionado_id is None:
                messagebox.showwarning("Aviso", "Selecione um guincho antes de solicitar.")
                return

            sucesso = model.inserir_solicitacao_de_guincho(placa_carro, local_de_origem, local_de_destino, '0', data,guincho_selecionado_id)

            if sucesso:
                messagebox.showinfo("Sucesso", "Solicitação feita com sucesso!")
                j_principal.destroy()
            else:
                messagebox.showerror("Erro", "Erro ao solicitar guincho.")

        for id_guincho, nome in guinchos:
            botao = tk.Button(
                j_principal,
                text=nome,
                width=30,
                command=lambda i=id_guincho: selecionar_guincho(i)
            )
            botao.grid(row=row_guincho, column=0, columnspan=2, padx=10, pady=2)
            row_guincho += 1

        label_guincho_selecionado = tk.Label(j_principal, text='Nenhum guincho selecionado')
        label_guincho_selecionado.grid(row=row_guincho, column=0, columnspan=2, pady=10)

        botao_solicitar = tk.Button(j_principal, text='Solicitar', command=inserir)
        botao_solicitar.grid(row=row_guincho + 1, column=0, columnspan=2, pady=15)

def abrir_j_princilpal_guincho():
    j_principal = tk.Toplevel()
    j_principal.title('')
    j_principal.geometry("500x400+200+200")

    text_principal = tk.Label(j_principal,text='Solicitações pendentes')
    text_principal.grid(row=0,column=0,padx=10,pady=10)

    lista_box = tk.Listbox(j_principal, width=60)
    lista_box.grid(row=1,column=0,padx=10,pady=10)
    
    registros = model.buscar_solicitacoes_guincho()
    
    for reg in registros:
        texto = f"ID: {reg[0]} | Placa: {reg[1]} | Origem: {reg[2]} | Destino: {reg[3]}"
        lista_box.insert(tk.END, texto)

    entry_id = tk.Entry(j_principal)
    entry_id.grid(row=2, column=0, padx=10, pady=10)

    def aceitar(status):
        id = entry_id.get()
        sucesso = model.aceitar_pedido(status,id)

        if sucesso:
            messagebox.showinfo("Sucesso", "Aceito com sucesso a solicitação!")
            j_principal.destroy()
        else:
            messagebox.showerror("Erro", "Erro na solicitação.")

    botao_aceitar = tk.Button(j_principal, text='Aceitar', command=lambda:aceitar(1))
    botao_aceitar.grid(row=3, column=0, padx=10, pady=10)

    botao_cancelar = tk.Button(j_principal, text='Cancelar', command=lambda:aceitar(2))
    botao_cancelar.grid(row=4, column=0, padx=10, pady=10)




