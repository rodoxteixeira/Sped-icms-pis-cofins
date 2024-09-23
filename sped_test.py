import openpyxl

# Carregar o arquivo Excel
workbook = openpyxl.load_workbook(r'C:\Users\DISTAC\Desktop\sped.xlsx')

# Selecionar as planilhas
plan1 = workbook['Plan1']
planilha1 = workbook['Planilha1']

# Valor a ser buscado na célula N2 da aba Plan1
valor_buscado = plan1['N2'].value

# Variável para armazenar o valor de retorno
valor_retorno = None

# Procurar o valor na coluna I da aba Planilha1 e pegar o valor correspondente da coluna B
for row in planilha1.iter_rows(min_row=2, max_col=10, values_only=True):
    if row[9] == valor_buscado:  # A coluna I é o índice 9 (começa de 0)
        valor_retorno = row[0]   # A coluna B é o índice 1
        break

# Atualizar a célula com o valor retornado, se encontrado
if valor_retorno:
    plan1['B2'] = valor_retorno
    print(f"Valor {valor_retorno} encontrado e atualizado na célula B2 de Plan1.")
else:
    print("Valor não encontrado na coluna n de Planilha1.")

# Salvar as alterações no arquivo
workbook.save(r'C:\Users\DISTAC\Desktop\python\sped_atualizado.xlsx')
print("Arquivo salvo com sucesso!")

