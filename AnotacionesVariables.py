#Recuerda no usar el nombre de una palabra reservada por ejemplo print

#No es posible hacer:
#print=print 

#Para consultar la lista de palabras revervadas podemos usar
import keyword
print(keyword.kwlist)

#La lista que saldrá será la siguiente: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#No iniciar con número
#30anios = 30 
#En su lugar se usa anios30 = 30

#Tampoco usar carácteres especiales
#Por ejemplo -, @, /.

#Tampoco llevan espacios
#mi edad = 30

#Usar camelCase
miEdad = 30
