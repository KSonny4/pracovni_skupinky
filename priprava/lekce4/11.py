cisla = [3, 5, 8, 9, 14]

def is_sorted(seznam):
  for i in range(len(seznam)-1):
    if seznam[i] > seznam[i+1]:
      return False
  return True

print(is_sorted(cisla))