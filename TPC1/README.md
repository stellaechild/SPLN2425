---
Título: TPC1
Data: 10/02/2025
Autor: Maria Cunha
UC: SPLN
---
# Filtro que Elimina Linhas Repetidas num Ficheiro

Modo de utilização : python3 tpc1.py /testes/[ficheiro]

Este código remove linhas duplicadas de ficheiros de formato .txt ou .pdf. Este utiliza o `pdftotext` para extrair texto de pdf's e processa o texto linha por linha, normalizando os espaços, removendo pontuação e convertendo para minúsculas. Assim considerou-se que frases seriam iguais de acordo com o seu conteúdo semântico, seguindo o exemplo: "SPLN é fixe!", "spln é fixe ", "Spln é fixe!". Por fim, depois de executado, será impremido para o terminal as linhas únicas, ignorando as repetidas. Por fim, o número de linhas únicas e removidas são apresentadas. 
