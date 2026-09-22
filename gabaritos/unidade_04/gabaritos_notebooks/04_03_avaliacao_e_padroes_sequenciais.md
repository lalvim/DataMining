# Gabarito — 04.03 Avaliação de regras de associação

## U04-NB03-V01

O *leverage* é uma diferença entre duas proporções de transações:

$$P(A\cap B)-P(A)P(B).$$

Assim, *leverage* 0,125 significa diferença absoluta de 0,125 na proporção conjunta, equivalente a 12,5 pontos percentuais acima do valor esperado sob independência. Não significa aumento relativo de 12,5% e muito menos aumento comprovado nas vendas. A métrica descreve a coocorrência na amostra e não estima o efeito causal de uma intervenção.

**Rubrica:** identificar diferença absoluta (1 ponto), usar pontos percentuais (1), rejeitar interpretação causal ou de aumento de vendas (1).

## U04-NB03-E01

Para $A=\{oleo\}$ e $B=\{feijao\}$, óleo aparece em 3 das 12 transações, feijão em 6 e ambos aparecem juntos em 3:

$$P(A)=\frac{3}{12}=0{,}25,\qquad P(B)=\frac{6}{12}=0{,}50,$$

$$P(A\cap B)=\frac{3}{12}=0{,}25.$$

O *leverage* é

$$0{,}25-(0{,}25\times0{,}50)=0{,}125.$$

Na Tabela 1, isso corresponde a 3 coocorrências observadas, $12\times0{,}25\times0{,}50=1{,}5$ esperada e excesso de $3-1{,}5=1{,}5$ transação. De fato, $12\times0{,}125=1{,}5$.

As três transações com óleo também contêm feijão, então

$$\operatorname{Confiança}(A\rightarrow B)=\frac{3}{3}=1.$$

Não há falhas observadas. Sob independência, seriam esperadas

$$3\,[1-P(B)]=3(1-0{,}50)=1{,}5$$

falha. Pela fórmula,

$$\operatorname{Conviction}(A\rightarrow B)=\frac{1-0{,}50}{1-1}=\frac{0{,}50}{0}=\infty.$$

Isso indica ausência de óleo sem feijão nas 12 transações observadas, não uma regra universal.

**Rubrica (8 pontos):** probabilidades (2), *leverage* e ligação à Tabela 1 (2), falhas observadas/esperadas (2), *conviction* e interpretação amostral (2).
