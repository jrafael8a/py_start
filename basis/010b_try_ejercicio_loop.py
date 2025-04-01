balance = 945.70
print(f'Balance Actual: {balance}')

while True:
    try:
        num = float(input('Deposito: '))
        break
    except ValueError:
        print('Must be a valid quantity.')
                                		
balance += num
print(f'Nuevo Balance: {balance}')