def decimal_para_binario(decimal):
    return bin(decimal).replace("0b", "")

def decimal_para_hexadecimal(decimal):
    return hex(decimal).replace("0x", "").upper()

def binario_para_decimal(binario):
    return int(binario, 2)

def binario_para_hexadecimal(binario):
    decimal = binario_para_decimal(binario)
    return decimal_para_hexadecimal(decimal)

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_para_binario(hexadecimal):
    decimal = hexadecimal_para_decimal(hexadecimal)
    return decimal_para_binario(decimal)

def main():
    print("Calculadora de Conversão")
    print("1. Decimal para Binário")
    print("2. Decimal para Hexadecimal")
    print("3. Binário para Decimal")
    print("4. Binário para Hexadecimal")
    print("5. Hexadecimal para Decimal")
    print("6. Hexadecimal para Binário")
    
    escolha = input("Escolha uma opção (1-6): ")
    
    if escolha == '1':
        decimal = int(input("Digite um número decimal: "))
        print(f"Binário: {decimal_para_binario(decimal)}")
    elif escolha == '2':
        decimal = int(input("Digite um número decimal: "))
        print(f"Hexadecimal: {decimal_para_hexadecimal(decimal)}")
    elif escolha == '3':
        binario = input("Digite um número binário: ")
        print(f"Decimal: {binario_para_decimal(binario)}")
    elif escolha == '4':
        binario = input("Digite um número binário: ")
        print(f"Hexadecimal: {binario_para_hexadecimal(binario)}")
    elif escolha == '5':
        hexadecimal = input("Digite um número hexadecimal: ")
        print(f"Decimal: {hexadecimal_para_decimal(hexadecimal)}")
    elif escolha == '6':
        hexadecimal = input("Digite um número hexadecimal: ")
        print(f"Binário: {hexadecimal_para_binario(hexadecimal)}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
