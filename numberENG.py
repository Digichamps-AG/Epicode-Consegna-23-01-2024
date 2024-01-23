# Scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'è altra strada che quella
# di prevedere una traduzione semplice attraverso una tabella:
# 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","one", "two", "three", "four", "five", "six", "seven",
               "eight", "nine", "ten", "elev", "twelve", "thirteen",
               "fourteen", "fifteen", "sixteen", "seventeen",
               "eighteen", "nineteen"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilitè/à di prevedere
# una "traduzione" della decina e demandare la "traduzione"
# dell'unitè/à alla funzione che traduce fino a 20
# 25 -> decina = 2, unitè/à = 5


def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["twenty", "thirty", "forty", "fifty", "sixty",
               "seventy", "eighty", "ninety"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unitè/à di 
    
    # ho aggiunto una condizione che gestisce i casi tipo: 21,31,41, ecc.: 

    #if unit == 1:     
    #    return DECADES[decade-2][:-1] + translate_to_20(unit)
    
    return DECADES[decade-2] + translate_to_20(unit)


#def translate_number(n):
 #   return translate_to_100(n)

#for x in range(1, 101):
#    print(translate_number(x))

def translate_to_1000(n):
    if n < 20:
        return translate_to_20(n)
    
    if n < 100:
        return translate_to_100(n)
    
    if n > 999:
        return("Out of range")

   
    CENTINAIA = ["hunderd", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
    cents = n // 100 

    decineUnità = n % 100  

    if n == 100:
        return "onehundred"
    
    if decineUnità <20: 
        return CENTINAIA[cents - 1] + translate_to_20(decineUnità)
   
    else: 
        return CENTINAIA[cents - 1] + translate_to_100(decineUnità)
    
    


def translate_to_10000(n):
    if n > 9999:
        return("Out of range")

    if n < 20:
        return translate_to_20(n)
    
    if n < 100:
        return translate_to_100(n)

    if n < 1000:
        return translate_to_1000(n)
    
    MIGLIAIA = ["thousand", "twothousand", "threethousand", "fourthousand", "fivethousand", "sixthousand", "seventhousand", "eightousand", "ninethousand"]

    miles = n // 1000 

    centDecUni = n % 1000 

   
    return MIGLIAIA[miles - 1] + translate_to_1000(centDecUni) 


print(translate_to_10000(9761).title())

x = "ciao"
print(x + " a tutti")