import sys
import re
import subprocess

__doc__ = '''
NAME
   repetidas - Remove ou comenta linhas repetidas de um arquivo de texto ou PDF

SYNOPSIS
   repetidas [options] input_files
   options:
    -s  Diferencia linhas com e sem espaços no final
    -e  Remove linhas vazias
    -p  Adiciona um prefixo '#' às linhas duplicadas em vez de removê-las (comenta)
    -h  Documentação

DESCRIPTION
   Remove ou comenta linhas repetidas de um arquivo de texto ou PDF, mantendo a saída no stdout.
'''

def processar_texto(linha, linhas_vistas, linhas_removidas, espacos_diferenciam, prefixo):
    linha_processada = linha.rstrip() if espacos_diferenciam else re.sub(r'\s+', ' ', linha.strip())
    
    if linha_processada:  
        if linha_processada not in linhas_vistas:
            linhas_vistas[linha_processada] = linha  
            print(linha, end='')
        else:
            linhas_removidas[0] += 1  
            if prefixo:
                print(f"# {linha}", end='')

def remover_linhas_repetidas(ficheiro, espacos_diferenciam, remover_vazias, prefixo):
    linhas_vistas = {}  
    linhas_removidas = [0]  
    
    def processar_fonte(texto):
        for linha in texto.splitlines():
            if remover_vazias and not linha.strip():
                continue
            processar_texto(linha, linhas_vistas, linhas_removidas, espacos_diferenciam, prefixo)
    
    try:
        if ficheiro.endswith('.pdf'):
            resultado = subprocess.run(['pdftotext', ficheiro, '-'], capture_output=True, text=True)
            processar_fonte(resultado.stdout)
        else:
            with open(ficheiro, 'r', encoding='utf-8') as f:
                processar_fonte(f.read())
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)
    
    print(f"\nTotal de linhas únicas: {len(linhas_vistas)}")
    print(f"Total de linhas repetidas {'comentadas' if prefixo else 'removidas'}: {linhas_removidas[0]}")

def main():
    if '-h' in sys.argv:
        print(__doc__)
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Por favor, forneça o caminho do arquivo.")
        sys.exit(1)

    ficheiro = sys.argv[1]

    espacos_diferenciam = '-s' in sys.argv
    remover_vazias = '-e' in sys.argv
    prefixo = '-p' in sys.argv

    print(f"Processando o arquivo: {ficheiro}")
    
    remover_linhas_repetidas(ficheiro, espacos_diferenciam, remover_vazias, prefixo)

if __name__ == '__main__':
    main()




