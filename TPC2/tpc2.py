import sys
import re
import argparse
#! /usr/bin/env python
from jjcli import *

def processar_texto(linha, linhas_vistas, linhas_removidas, args):
    linha_original = linha.rstrip('\n')
    linha_limpa = re.sub(r'\s+', ' ', linha.strip())
    linha_limpa = re.sub(r'[^\w\s]', '', linha_limpa)
    linha_limpa = linha_limpa.lower()

    print(f"Processing line: {linha_original}")  # Debug

    if args.e and not linha_limpa:
        return  
    
    if linha_limpa:
        if linha_limpa not in linhas_vistas:
            linhas_vistas.add(linha_limpa)
            print(linha_original)  # Print unique lines
        else:
            linhas_removidas[0] += 1
            if args.p:
                print(f"{args.p}{linha_original}")  # Print repeated lines with prefix
    elif not args.e:
        print(linha_original)  # Print empty or non-cleaned lines

def remover_linhas_repetidas(cli, args):
    linhas_vistas = set()
    linhas_removidas = [0]

    # Try using the text() method to get the content
    print(f"Reading lines using cli.text()...")

    # Using cli.text() to get the text content from the clfilter object
    content = cli.text()  # Get content using text method
    
    # Now iterate over the content (if it's a string, split it into lines)
    for linha in content.splitlines():  # Assuming content is a string, we split it by lines
        processar_texto(linha, linhas_vistas, linhas_removidas, args)
    
    print(f"\nTotal de linhas únicas: {len(linhas_vistas)}")
    print(f"Total de linhas repetidas encontradas: {linhas_removidas[0]}")

def main():
    cl = clfilter(opt="sep", man=__doc__)  # Initialize clfilter
    parser = argparse.ArgumentParser(
        description="Remove ou comenta linhas duplicadas de um arquivo de texto ou PDF.",
        epilog="Exemplo de uso: python3 script.py exemplo.txt"
    )
    parser.add_argument("ficheiro", help="O arquivo de texto ou PDF para processar.")
    parser.add_argument("-s", action="store_true", help="Diferencia linhas em branco de linhas com espaços.")
    parser.add_argument("-e", action="store_true", help="Remove linhas em branco do arquivo.")
    parser.add_argument("-p", metavar="PREFIXO", type=str, help="Adiciona um prefixo às linhas repetidas, por exemplo, '#'" )
    
    args = parser.parse_args()
    
    # Use clfilter to get a filtered iterator or file-like object
    cli = clfilter(args.ficheiro)  # Get the clfilter object
    
    # Process the file with clfilter object
    remover_linhas_repetidas(cli, args)

if __name__ == "__main__":
    main()


