periodo = 13
continua = True 

valor  = int (input ("Valor inicial de nascimento:R$"))
valorDep = int (input ("Valor mensal de deposito:R$"))
taxa = float (input("Taxa de juros Mensal:%"))

while (continua):
  for j in range(1,periodo) :
    valor = valor + valor * taxa + valorDep
    print (j,"%.2f" % valor) 

  resp = input ("Deseja simular proximo ano? [s/n]:")
  if(resp == "n"):
    continua = False