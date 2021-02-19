## PARTE 1
Sistema que voce consegue estudar, onde e possivel estudar variaveis aleatorias e deterministicas (nao aleatorias), iss é um processo estocastico, uma fila é um, pois há duas variaveis, o tempo entre as chegadas (aleatoria geralmente, mas pode ser deterministico caso seja tempos "fixos"), 


SEMPRE 5 intervalos (Classes), intervalos iguais;
-ln(random(i)) * 15, usa essa formula para gerar os TECs


Tempo de chegada no relogio (do tempo que abriu o banco) TEC = Tempo de chegada no relogio do anterior + TEC atual
Tempo = tempo na fila + tempo para ser atendido
Tempo fim de serviço = Tempo inicio serviço + TS
Tempo no sistema = Tempo na fila + TS


2º cliente
Gera o TEC, gera o TS, joga na tabela
Tempo de chegada no relogio = Tec(2) + Tec(1)

Sempre ter em mente que há um periodo que o banco fica aberto

Intervalo de tempo:
colocamos um periodo, abre x horas e fecha y horas, nao é algo que fica 24 horas aberto. Caso fique 24h acaba gerando uma fila muito grande,
abre as 10h e fecha as 15h. Criamos um intervalo menor.
1000 segundos, 30 minutos é suficiente



## PARTE 2
Usar sementes diferentes para obter resultados diferentes e depois tirar as medias das medias.
Para cada semente, teremos uma media (tempo medio no sistema, tempo medio de atendimento, ...)
E depois, como usaremos varias sementes, calcular a media dessas medias, calcular tambem o desvio padrao.
Calcular o intervalo de confiança, nivel de significancia (alpha) será 5% (0.05), n = numero de sementes diferentes utilizadas (replicas)
Usar no minimo 121 sementes diferentes, 1.96 caso use 121 sementes (isso é tabelado), tentar pegar 121 sementes aleatorias

## PARTE 3 - RELATORIO
1. Objetivos
2. Resumo
3. Introdução teórica (O que é simulação? Por que simular um
sistema? Aplicações das simulações, etc.)
4. Metodologia
    * Modelo conceitual: dados de entrada, distribuições de
    probabilidade, hipóteses e detalhamento do sistema ou o que
    foi assumido, medidas de desempenho, limitações de tempo
    e recursos computacionais, fluxograma, validação do modelo
    conceitual.
    * Modelo computacional: Código fonte documentado – de modo
    que outra pessoa possa entendê-lo. Especificar as etapas de
    cada execução. Verificar a duração do período inicial instável.
    Excluir o período instavel das medidas (regime transiente).
5.Documentar os resultados – Apresentar os dados obtidos
através de tabelas, gráficos, etc. Apresentar uma breve
discussão sobre os resultados obtidos. Apresentar o código fonte.