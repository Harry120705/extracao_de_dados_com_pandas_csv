import pandas as pd

# Lista de números de inscrição para extrair
inscricoes = [
20250000001, 20250000002, 20250000003, 20250000004, 20250000005
]

try:
    # Ler o arquivo CSV que casualmente nomeei como
    df = pd.read_csv('Dados.csv')

    # Filtrar o DataFrame para manter apenas as linhas com as inscrições desejadas
    dados_extraidos = df[df['INSCRICAO'].isin(inscricoes)]

    # Salvar os dados extraídos em um novo arquivo CSV
    dados_extraidos.to_csv('dados_extraidos.csv', index=False)

    print("Dados extraídos com sucesso e salvos no arquivo 'dados_extraidos.csv'")

except FileNotFoundError:
    print("Erro: O arquivo 'Dados.csv' não foi encontrado. Certifique-se de que ele está na mesma pasta que o script.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")