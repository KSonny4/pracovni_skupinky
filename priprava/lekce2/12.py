import sys
import random
#12. A) Napište program, který při každém spustění hodí šestistěnnou kostkou ‒ tedy vypíše náhodné číslo mezi 1 až 6.
print(random.randint(1,6))

#12. B) Upravte program tak, aby jako parametr dostal počet stěn kostky. Bude tedy umět házet třeba sedmistěnnou nebo devítistěnnou kostkou podle toho, jaké číslo dostane na vstupu.
number = int(sys.argv[1])
print (str(random.randint(1,number)))

#12. C) Předejte programu další parametr, který bude udávat kolik hodů má program provést. Program pak na výstup vytiskne seznam tolika hodů, kolik jste zadali na vstupu. Cílem je tedy vymyslet, jak vyrobit seznam náhodných čísel. Jistě se nám k tomu bude hodit chroustání seznamů.
number = int(sys.argv[1])
repeat = int(sys.argv[2])
solution1 = [random.randint(1,number) for i in [1] * repeat]
print(solution1)
solution2 = [random.randint(1,number) for i in range(repeat)]
print(solution2)