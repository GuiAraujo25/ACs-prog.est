def ordenar_strng(strings):
  return sorted(strings, key=lambda x: len(x), reverse=True)

def main():
  num_casos_teste = int(input())
  
  for _ in range(num_casos_teste):
    conjunto_strings = input().split()

    if len (conjunto_strings) < 1 or len(conjunto_strings) > 50:
      print("Número de strings deve ser maior que 0 e menor que 51")
      return

    for string in conjunto_strings:
      if len (string) < 1 or len(string) > 50:
        print("Número de caracteres da string deve ser maior que 0 e menor que 51")
        return

    conjunto_ordenado = ordenar_strng(conjunto_strings)
    print(" ".join(conjunto_ordenado))

if __name__ == "__main__": 
  main()