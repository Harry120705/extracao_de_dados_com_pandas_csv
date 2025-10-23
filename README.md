# extracao_de_dados_com_pandas_csv

Este repositório contém scripts em Python desenvolvidos para realizar a extração e a validação de dados de um arquivo CSV, demonstrando uma solução prática para um desafio real onde ferramentas de IA não foram suficientes.

## O Problema

O objetivo inicial era simples: filtrar um arquivo `Dados.csv` para extrair **339 registros** específicos, identificados por seus números de inscrição. A primeira abordagem foi utilizar a IA do Gemini para agilizar a tarefa, um método que já havia funcionado com sucesso em extrações de dados anteriores.

No entanto, desta vez, a ferramenta não conseguiu processar a solicitação, mesmo com o arquivo sendo enviado para a plataforma. Essa falha inesperada me levou a desenvolver uma solução local, com total controle sobre o processo.

## A Solução em Duas Etapas

Diante do obstáculo, a solução foi dividida em duas fases, cada uma com seu próprio script.

### Etapa 1: Extração dos Dados (`Extracao.py`)

O primeiro script, **`Extracao.py`**, foi criado para executar a tarefa principal: ler o arquivo `Dados.csv` e filtrar apenas as linhas que correspondiam aos 339 números de inscrição fornecidos.

Ao executá-lo, o script funcionou perfeitamente, mas trouxe um resultado intrigante: o arquivo de saída continha apenas **291 registros**, e não os 339 esperados. Após verificação percebi que 48 códigos não foram encontrados.

### Etapa 2: Verificação e Auditoria (`verificar_faltantes.py`)

Para investigar a discrepância, foi desenvolvido um segundo script, **`verificar_faltantes.py`**. Sua única finalidade era auditar os dados, comparando a lista original de inscrições com os dados presentes no CSV.

Este script identificou e retornou a lista exata dos **códigos faltantes**, confirmando que eles não existiam na base de dados original e concluindo a análise.

## Estrutura do Projeto

```
/
├── Dados.csv               # Arquivo original com todos os dados (não incluído por padrão)
├── Extracao.py             # Script 1: Extrai os dados encontrados
├── verificar_faltantes.py    # Script 2: Identifica os códigos não encontrados
└── README.md               # Este arquivo
```

## Pré-requisitos

Para executar os scripts, você precisará ter o Python instalado em seu sistema, juntamente com a biblioteca `pandas`.

  - **Python 3.x**
  - **Pandas**:
    ```bash
    pip install pandas
    ```

## Como Usar

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Adicione o arquivo de dados:** Coloque o seu arquivo `Dados.csv` na pasta raiz do projeto.

3.  **Execute o script de extração:** Para filtrar o arquivo e gerar `dados_extraidos.csv`, execute:

    ```bash
    python Extracao.py
    ```

    Isso criará um novo arquivo chamado `dados_extraidos.csv` contendo os 291 registros encontrados.

4.  **Execute o script de verificação (opcional):** Para identificar quais códigos não foram encontrados, execute:

    ```bash
    python verificar_faltantes.py
    ```

    Este comando irá imprimir no terminal a lista dos 48 códigos faltantes e também salvará essa lista no arquivo `inscricoes_nao_encontradas.txt`.

## Conclusão

Este projeto é um exemplo prático de como a habilidade de desenvolver soluções personalizadas com scripting é fundamental. Embora ferramentas de IA sejam extremamente úteis, a capacidade de analisar um problema, construir uma solução sob medida e iterar sobre os resultados é o que garante a precisão e a profundidade na manipulação de dados.
