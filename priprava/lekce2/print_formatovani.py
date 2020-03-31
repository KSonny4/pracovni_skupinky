seznam = [1,2,3]
slovo = "AHOJ SVETE"

# funguje, vypisuju seznam
print(seznam)

# funguje, vypisuju string (retezec)
print(slovo)

#NEFUNGUJE, snazim se udelat operaci + na string a list
# dostanu chybu TypeError: can only concatenate str (not "list") to str
# takze tohle prosim vyhodte a muzete pustit program
print("tohle je seznam: " + seznam)

#musim bud pouzit zabalit seznam to str
print("tohle je seznam: " + str(seznam))

#nebo pouzit format
print("tohle je seznam: {}".format(seznam))

#ale uplne nejlepsi je f-string
print(f"tohle je seznam: {seznam}")

