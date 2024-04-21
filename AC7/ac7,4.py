Numero = int(input())

if Numero > 50:
  print("Este valor é maior que 50.")
else:
  N = [0] * 10
  N[0] = Numero

  for i in range(1, 10):
      N[i] = N[i - 1] * 2

  i = 0
  while i < 10:
      print(f"N[{i}] = {N[i]}")
      i += 1
