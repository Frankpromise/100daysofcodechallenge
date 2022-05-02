print('Welcome to my online tip calculator')
bill = float(input('How much is your bill?\n'))
tip = float(input('What is the percentage of tip you will give? 0, 12, 15, 20\n'))
people = float(input('How many people will share the bill?\n'))

tip_calculator = (bill * tip)/100
total_bill = (tip_calculator + bill)/people

print(f'Each person pays ${total_bill}')
