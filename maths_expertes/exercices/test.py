
dividende_initial = 20041010127834023843100
dividende = dividende_initial
diviseur_initial = 97
diviseur = 1
quotient = 0
rest = 0
loop = 1

while dividende >= diviseur_initial:

    diviseur = diviseur_initial
    loop = 1
    print(dividende)

    if diviseur * 100 <= dividende:

        print("\t #", diviseur, " * 100 <= ", dividende)

        while diviseur * 10 <= dividende:
            diviseur *= 10
            loop *= 10

    else:

        print("\t #", diviseur, " * 100 > ", dividende)

        while diviseur <= dividende:
            dividende -= diviseur
            diviseur += diviseur
            loop += 1

    print("diviseur = ", diviseur, "\nloop = ", loop, "\ndividende = ", dividende, '\n')
    quotient += loop

    rest = dividende_initial - (diviseur_initial * quotient)
    dividende = rest
print(dividende_initial, ' = ', quotient, ' * ', diviseur_initial, ' + ', rest)