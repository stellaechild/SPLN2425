---
Título: TPC2
Data: 15/02/2025
Autor: Maria Cunha
UC: SPLN
---
# Filtro que Elimina Linhas Repetidas num Ficheiro
```txt
Modo de utilização : python3 tpc2.py [option*] /testes/[ficheiro]
                   | repetidas [option*] /testes/[ficheiro]

option:
        -s  Diferencia linhas com e sem espaços no final
        -e  Remove linhas vazias
        -p  Adiciona um prefixo '#' às linhas duplicadas em vez de removê-las (comenta)
        -h  Exibe a documentação
```

A segunda opção é possível devido aos seguintes comandos:

ln -s ~/SPLN2425/TPC2/tpc2.py /usr/local/bin/repetidas

chmod +x ~/SPLN2425/TPC2/tpc2.py

