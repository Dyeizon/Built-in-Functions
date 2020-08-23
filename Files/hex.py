# hex(x)
# Converte um número inteiro para uma String hexadecimal em minúsculo prefixada com "0x".

# Normal
print(hex(160))

# Sem o prefixo
print("{:x}".format(int(160)))

# Maiúsculo
print("{:X}".format(int(3735928559)))