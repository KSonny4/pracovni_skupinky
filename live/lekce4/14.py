import sys

seznam = sys.argv[1:]
seznam = [int(x) for x in seznam]
print(f" nas seznam {seznam}")
serazeny = sorted(seznam)
print(f" 2. nejvetsi prvek {serazeny[-2]}")


# seradime
seznam_set = sorted(seznam)

# udelame z toho set --> jako distinct v sql
# set nejde indexovat, musime ho prevest na list
seznam_set = list(set(seznam_set))
print(f"seznam : {seznam_set}")
print(f"SET!! 2 nejvetsi max: {seznam_set[-2]}")