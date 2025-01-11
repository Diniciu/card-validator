import re

def validar_cartao(numero):
    # Remove espaços e hifens
    numero = re.sub(r'[\s-]', '', numero)
    
    # Verifica se o número contém apenas dígitos
    if not numero.isdigit():
        return False, "Número inválido!"

    # Algoritmo de Luhn para validação do número do cartão
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    if luhn_checksum(numero) != 0:
        return False, "Número inválido!"

    # Identificação da bandeira do cartão
    bandeiras = {
        "American Express": r"^3[47][0-9]{13}$",
        "Aura": r"^50[0-9]{14,17}$",
        "Cartão C6": r"^636297[0-9]{10}$",
        "Cartão Will Bank": r"^5067[0-9]{12}$",
        "Cartão XP": r"^6375[0-9]{12}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "Elo": r"^((636368)|(438935)|(504175)|(451416)|(636297)|(5067)|(4576)|(4011))\d{0,10}$",
        "EnRoute": r"^(2014|2149)[0-9]{11}$",
        "Hipercard": r"^(606282\d{10}(\d{3})?)|(3841\d{15})$",
        "Itaú Credicard": r"^6370[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Maestro": r"^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "Nubank": r"^6034[0-9]{12}$",
        "Santander Free": r"^6042[0-9]{12}$",
        "UnionPay": r"^62[0-9]{14,17}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "Voyager": r"^8699[0-9]{11}$"
    }
    
    for bandeira, regex in bandeiras.items():
        if re.match(regex, numero):
            return True, bandeira
    
    return False, "Bandeira desconhecida"

# Solicita o número do cartão ao usuário
print("=" * 37)
numero_cartao = input("Digite o número do cartão de crédito: ")
valido, bandeira = validar_cartao(numero_cartao)
print(f"Válido: {valido}; Bandeira: {bandeira}.")