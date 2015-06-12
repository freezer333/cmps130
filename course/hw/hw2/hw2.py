def build_periodic_table(filename="periodic_table.txt"):
	input_file = open(filename, 'r')
	table = dict()
	for element in input_file:
		tokens = element.split()
		table[tokens[2]] = (tokens[1], int(tokens[0]), float(tokens[3]))
	return table

def calc_mass(table, formula):
	mass = 0
	for e in formula:
		if e[0] not in table:
			raise ValueError(e + " not a valid element")
		mass += table[e[0]][2] * e[1]
	return mass

def search_by_string(table, search):
	results = []
	for symbol in table:
		if symbol.upper().find(search.upper()) >= 0 :
			results.append((symbol,) + table[symbol])
		elif table[symbol][0].upper().find(search.upper()) >= 0:
			results.append((symbol,) + table[symbol])
	return results

def search_by_mass(table, minmass, maxmass):
	results = []
	for symbol in table:
		mass = table[symbol][2]
		if mass >= minmass and mass <= maxmass:
			results.append((symbol,) + table[symbol])
	return results

def print_results(results):
	print('{:>5}'.format("#"), end="  ")
	print('{:<30}'.format("Element name"), end="")
	print('{:<5}'.format("Sym"), end="")
	print('{:<5}'.format("Mass"))
	print("="*80)
	for e in results:
		print('{:>5}'.format(e[2]), end="  ")
		print('{:<30}'.format(e[1]), end="")
		print('{:<5}'.format(e[0]), end="")
		print('{:<5}'.format(e[3]), end="")
		print()
	print("="*80)

table = build_periodic_table()
print("Loaded Periodic Table!")
selection = 0
while selection != 4:
	print("1) Search by symbol/name")
	print("2) Search by atomic mass")
	print("3) Molecular Mass Calculation")
	print("4) Quit")
	
	selection = int(input("Please enter choice:  "))

	if selection == 1:
		results = search_by_string(table, input("Please enter search string:  "))
		print_results(results)
	elif selection == 2:
		results = search_by_mass(table, float(input("Please enter minimum mass:  ")), float(input("Please enter maximum mass:  ")))
		print_results(results)
	elif selection == 3:
		symbol = ""
		formula = []
		while symbol != ".":
			symbol = input("Enter atomic symbol of element:  ")
			if symbol != ".":
				num = int(input("Enter number of atoms of "+  symbol + " in molecule:  "))
				formula.append((symbol, num))
		mass = calc_mass(table, formula)
		print("The molecular mass is ", mass)
	else :
		exit()