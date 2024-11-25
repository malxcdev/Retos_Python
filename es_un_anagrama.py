def is_anagrama(primera_palabra, segunda_palabra):
    #contemos las letras
    if len(primera_palabra) == len(segunda_palabra):
        next
    else:
        return False
    
    #ordenemos las letras
    palabra_ordenada1 = sorted(primera_palabra.lower())
    palabra_ordenada2 = sorted(segunda_palabra.lower())

    if palabra_ordenada1 == palabra_ordenada2:
        return True
    else:
        return False
    

print(is_anagrama("mora","roma"))