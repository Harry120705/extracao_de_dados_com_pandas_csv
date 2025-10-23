import pandas as pd
# Lista de números de inscrição para comparar
inscricoes_usuario = [
    20250000001, 20250000002, 20250000003, 20250000004, 20250000005
]

try:
    # Ler o arquivo CSV principal
    df = pd.read_csv('Dados.csv')

    # Criar uma "set" (conjunto) com as inscrições do arquivo para uma busca rápida
    inscricoes_no_arquivo = set(df['INSCRICAO'])

    # Encontrar quais inscrições da sua lista NÃO estão no arquivo
    nao_encontrados = []
    for inscricao in inscricoes_usuario:
        if inscricao not in inscricoes_no_arquivo:
            nao_encontrados.append(inscricao)

    # Imprimir os resultados
    if nao_encontrados:
        print(f"Total de {len(nao_encontrados)} inscrições não encontradas:")
        for inscricao in nao_encontrados:
            print(inscricao)
        
        # Salva a lista em um arquivo de texto
        with open('inscricoes_nao_encontradas.txt', 'w') as f:
            for inscricao in nao_encontrados:
                f.write(f"{inscricao}\n")
        print("\nUma lista com essas inscrições foi salva no arquivo 'inscricoes_nao_encontradas.txt'")

    else:
        print("Todas as inscrições da sua lista foram encontradas no arquivo.")

except FileNotFoundError:
    print("Erro: O arquivo 'Dados.csv' não foi encontrado. Certifique-se de que ele está na mesma pasta que este script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")