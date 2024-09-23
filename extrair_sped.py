import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def extrair_dados_sped(filepath):
    nfe_entrada = []
    nfe_saida = []
    cte = []

    with open(filepath, 'r') as file:
        for line in file:
            campos = line.split('|')
            registro = campos[1]
            
            if registro == 'C100':  # Documento fiscal - entrada/saída
                chave = campos[9]
                numero = campos[8]
                if campos[2] == '0':  # Entrada
                    nfe_entrada.append((chave, numero))
                elif campos[2] == '1':  # Saída
                    nfe_saida.append((chave, numero))
            elif registro == 'D100':  # Conhecimento de transporte
                chave = campos[10]
                numero = campos[9]  # Corrigido para campo 9 para o número do CT-e
                cte.append((chave, numero))

    return nfe_entrada, nfe_saida, cte

def salvar_dados(data, tipo, output_folder):
    filename = f"{tipo}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(output_folder, filename)
    with open(filepath, 'w') as file:
        for chave, numero in data:
            file.write(f"{chave},{numero}\n")

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Selecionar o arquivo SPED
    input_filepath = filedialog.askopenfilename(title="Selecione o arquivo SPED",
                                                filetypes=(("Arquivos SPED", "*.txt"), ("Todos os arquivos", "*.*")))
    if not input_filepath:
        messagebox.showerror("Erro", "Nenhum arquivo SPED selecionado.")
        return

    # Selecionar o diretório de saída
    output_folder = filedialog.askdirectory(title="Selecione o diretório onde salvar o resultado")
    if not output_folder:
        messagebox.showerror("Erro", "Nenhum diretório de saída selecionado.")
        return

    output_folder = os.path.join(output_folder, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    os.makedirs(output_folder, exist_ok=True)

    nfe_entrada, nfe_saida, cte = extrair_dados_sped(input_filepath)
    
    salvar_dados(nfe_entrada, 'NFe_Entrada', output_folder)
    salvar_dados(nfe_saida, 'NFe_Saida', output_folder)
    salvar_dados(cte, 'CTe', output_folder)
    
    messagebox.showinfo("Sucesso", f"Arquivos gerados com sucesso em {output_folder}")

if __name__ == "__main__":
    main()
