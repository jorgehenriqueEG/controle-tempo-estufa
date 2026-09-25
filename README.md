# controle-tempo-estufa
## Descrição do Problema
Sistema para registrar leituras de temperatura de estufas agrícolas e calcular a média diária com alerta de estresse térmico.
## Requisitos
* Receber lista de tuplas com horário e temperatura
* Calcular a média aritmética das temperaturas
* Identificar se houve período de calor extremo (acima de 35C)
## Exemplo de Uso
Entrada: [("08:00", 28.5), ("12:00", 36.2), ("16:00", 33.1)]
Saída: Media: 32.6C | Alerta: Sim