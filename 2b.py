def Bin2dec(binary):
    decimal = int(binary, 2)
    return decimal


def oct2hex(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)
    return hexadecimal


binary_input = input("Enter the Binary Number: ")
decimal_result = Bin2dec(binary_input)
print("Binary to Decimal is", decimal_result)

octal_input = input("Enter the Octal Number: ")
hexadecimal_result = oct2hex(octal_input)
print("Octal to Hexadecimal is", hexadecimal_result)
