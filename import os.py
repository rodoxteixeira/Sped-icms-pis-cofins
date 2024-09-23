import os
import shutil
import xml.etree.ElementTree as ET

# Diretórios
entrada = r'C:\Users\DISTAC\Desktop\VECTRON\xml'
saida = r'C:\Users\DISTAC\Desktop\VECTRON\resultados'

# Cria a pasta de saída se não existir
if not os.path.exists(saida):
    os.makedirs(saida)

def verificar_exclusao_pis_cofins(arquivo):
    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        pis_excluido = False
        cofins_excluido = False

        for pis in root.findall(".//PIS"):
            cst_element = pis.find(".//CST")
            if cst_element is not None and cst_element.text in ['04', '06', '07', '08', '09']:
                pis_excluido = True
                break

        for cofins in root.findall(".//COFINS"):
            cst_element = cofins.find(".//CST")
            if cst_element is not None and cst_element.text in ['04', '06', '07', '08', '09']:
                cofins_excluido = True
                break
        
        return pis_excluido and cofins_excluido
    except ET.ParseError:
        print(f"Erro ao processar o arquivo: {arquivo}")
        return False
    except Exception as e:
        print(f"Erro desconhecido ao processar o arquivo {arquivo}: {e}")
        return False

# Lê todos os arquivos XML na pasta de entrada
arquivos_processados = 0
arquivos_encontrados = 0

for arquivo in os.listdir(entrada):
    if arquivo.endswith('.xml'):
        caminho_completo = os.path.join(entrada, arquivo)
        arquivos_processados += 1

        # Verifica se o XML possui exclusão de PIS e COFINS
        if verificar_exclusao_pis_cofins(caminho_completo):
            arquivos_encontrados += 1
            # Copia o arquivo para a pasta de resultados
            shutil.copy(caminho_completo, saida)

print(f"Total de arquivos processados: {arquivos_processados}")
print(f"Arquivos com exclusão de PIS e COFINS encontrados: {arquivos_encontrados}")
print("Processamento concluído.")

