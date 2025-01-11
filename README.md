<h1>Explicação do Código</h1>
<h2>Script Python que valida um número de cartão de crédito e identifica sua bandeira (por exemplo, Visa, MasterCard):</h2>

  1. O script começa importando o módulo 're', que fornece suporte para expressões regulares, usadas para corresponder padrões em strings.

  2. A função 'validar_cartao' é definida para receber um número de cartão de crédito como entrada e validá-lo.

  3. Dentro da função, espaços e hifens são removidos do número de entrada para garantir que esteja em um formato limpo.

  4. Em seguida, o código verifica se o número contém apenas dígitos. Se o número contiver quaisquer caracteres não numéricos, a função retorna <b>False</b> e uma mensagem de erro.

  5. O algoritmo de Luhn é implementado como uma função aninhada dentro de 'validar_cartao'. Este algoritmo calcula o checksum de Luhn para validar o número do cartão de crédito. Se o checksum não for zero, o número é considerado inválido.

  6. O código verifica o checksum de Luhn. Se o checksum de Luhn não for zero, a função retorna <b>False</b> e uma mensagem de erro.

  7. Um dicionário é definido para mapear as bandeiras dos cartões para suas respectivas expressões regulares. Essas expressões regulares são usadas para corresponder o formato do número do cartão.

  8. O código então itera sobre o dicionário e usa expressões regulares para corresponder o número do cartão com a bandeira correta. Se uma correspondência for encontrada, a função retorna <b>True</b> e o nome da bandeira.

  9. Se nenhuma correspondência for encontrada, a função retorna <b>False</b> e uma mensagem de "bandeira desconhecida".

  10. Fora da função, o código solicita ao usuário que insira um número de cartão de crédito. O número inserido é validado usando a função 'validar_cartao', e o resultado é impresso, indicando se o cartão é válido e qual é a sua bandeira.
