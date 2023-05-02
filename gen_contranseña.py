
import string

from random import choices,shuffle,choice

while True:

    signos=choices(['@' , '#' , "?" , "¿" '¡' , "!" , '*' , '/' , '-' , '_'],k=3)

    letras=choices(string.ascii_letters+ string.ascii_uppercase,k=5)

    prim_letras=choices(string.ascii_letters + string.ascii_uppercase,k=2)

    cuerpo=*signos,*letras

    todo=*prim_letras,*cuerpo

    input("Presiona enter para generar una contraseña: ")

    if input:

       at=str(prim_letras),str(cuerpo)

       print(*todo,sep="")



    
    
    
   
    
    

 
    



