# Python: Operações com data e hora
## Epoch
- Contado em mili/segundos.
### Unix Epoch
- Utilizado em sistemas Unix, define o início do tempo como 00:00:00 UTC de 1/Jan/1970.
### Windows Epoch (ou "FileTime Epoch")
- Utilizado no Windows, é definido como 00:00:00 UTC em 1/Jan/1601.

## Data atual em relação ao Epoch
````
import time

tempo_atual = int(time.time())
print("O Tempo atual desde Unix Epoch:", tempo_atual)
# Segundos totais desde 00:00:00 UTC de 1/Jan/1970
````
## Gerar data a partir de float (epoch)
- "timestamp" é a representação de um ponto específico no tempo, geralmente expressa como o número de segundos decorridos desde o epoch.
````
import datetime

tempo_float = 1647936000.0  # 21/03/2022 às 00:00:00 UTC

# Método para converter o ponto flutuante em data
data_hora = datetime.datetime.utcfromtimestamp(tempo_float)

print("Data gerada:", data_hora)
````
## Criando datas
````
import datetime

data_atual = datetime.date.today()
print(f'Data atual: {data_atual}')

data_especifica = datetime.date(2024, 5, 9)
print(f'Data específica: {data_especifica})
````
## Operando com datas
````
import datetime

data_atual = datetime.datetime.now()

data_futura = data_atual + datetime.timedelta(days=7)
# Uma semana adiante em comparação à "data_atual"
````
## Formatando datas para string
- [Tabela de referência oficial](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
- [Tabela com exemplos](https://strftime.org/)
````
# Formatar data como string
data_formatada = data_atual.strftime("%d/%m/%Y")
````
## Formatando uma string para data
````
# Converter uma string em objeto de data
data_string = "2024-05-09"
data_objeto = datetime.datetime.strptime(data_string, "%Y-%m-%d")
````
## Dia da semana
````
import datetime

data = datetime.date(2024, 5, 9)

# 0 = segunda, 1 = terça ... 6 = domingo
dia_da_semana = data.weekday()
````
