n = 0
run = True
rest = 0
while run:
	rest = 3 ** (n + 1) % 7
	print("calcul : {0} : {1}".format(n, rest))
	
	if rest == 0:
		print('\t\t=============\n\t\tLa valeur de n est {}\n\t\t============='.format(n))
		run = False
	else:
		n += 1
