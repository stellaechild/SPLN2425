import sys
import re
import argparse
import subprocess

def processar_texto(linha, linhas_vistas, linhas_removidas):
    # Normaliza os espaços, remove pontuação e converte para minúsculas
    linha_limpa = re.sub(r'\s+', ' ', linha.strip())  # Normaliza os espaços
    linha_limpa = re.sub(r'[^\w\s]', '', linha_limpa)  # Remove pontuação
    linha_limpa = linha_limpa.lower()  # Converte para minúsculas para evitar diferenças de maiúsculas/minúsculas

    if linha_limpa:  # Verifica se a linha não está vazia
        if linha_limpa not in linhas_vistas:
            linhas_vistas.add(linha_limpa)  # Adiciona linha limpa ao conjunto

            # Imprime a linha original (sem modificações) para a saída
            print(linha, end='')
        else:
            linhas_removidas[0] += 1  # Conta as linhas repetidas, com lista para referência

def remover_linhas_repetidas(ficheiro):
    linhas_vistas = set()  # Conjunto para manter as linhas limpas únicas
    linhas_removidas = [0]  # Contador de linhas repetidas removidas, agora uma lista para referência
    
    # Deteta se é um pdf ou arquivo de texto
    if ficheiro.endswith('.pdf'):
        try:
            # Usando pdftotext via subprocess
            resultado = subprocess.run(['pdftotext', ficheiro, '-'], capture_output=True, text=True)
            texto_pdf = resultado.stdout  # Texto extraído do pdf
            
            # Processa o texto extraído do pdf
            for linha in texto_pdf.splitlines():
                processar_texto(linha, linhas_vistas, linhas_removidas)
        except Exception as e:
            print(f"Erro ao ler o PDF: {e}")
            sys.exit(1)
    else:
        try:
            with open(ficheiro, 'r', encoding='utf-8') as f:
                for linha in f:
                    processar_texto(linha, linhas_vistas, linhas_removidas)
        except Exception as e:
            print(f"Erro ao ler o arquivo de texto: {e}")
            sys.exit(1)

    # Exibe o total de linhas únicas e o número de linhas removidas
    print(f"\nTotal de linhas únicas: {len(linhas_vistas)}")
    print(f"Total de linhas iguais removidas: {linhas_removidas[0]}")

if __name__ == "__main__":
    # Argumentos
    parser = argparse.ArgumentParser(
        description="Remove linhas duplicadas de um arquivo de texto ou pdf.",
        epilog="Exemplo de uso: python3 tpc1.py exemplo.txt"
    )
    parser.add_argument("ficheiro", help="O arquivo de texto ou pdf para processar.")
    
    args = parser.parse_args()

    remover_linhas_repetidas(args.ficheiro)








