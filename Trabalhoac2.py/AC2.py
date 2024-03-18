#Exerccio 1A)
def eq_segundo_grau(a, b, c):
    delta = (b**2 - 4*a*c)
    x1 = ((-b + delta**0.5) / 2*a)
    x2 = ((-b - delta**0.5) / 2*a)
    print("A primeira raiz é:", x1)
    print("A segunda raiz é:", x2)

    eq_segundo_grau(5,8 ,23)



#Exercicio 1B)
def bissexto(ano):

   if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:  
       print("O ano é bissexto")
   else:
       print("O ano não é bissexto")
         


  #Exercício 2:
def calcular_salario(valor_hora, num_horas, irpf = 0.275):
   salario_líquido = (valor_hora * num_horas -(valor_hora * num_horas * irpf))
   print(salario_líquido)
    

calcular_salario(5, 4)
