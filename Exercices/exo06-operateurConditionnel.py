A = 3
B = 9
C = False
D = not (C)
E = 9

# Traitement

print(A > 8)
#// (1) = Faux

print(B == 9) 
# // (2) =

print(not(A != 3))
#// (3) =  

print(not(C) )
#// (4) =

print((A < B) or C )
#// (5) =

print(not((A + B) != 12))
#// (6) =

print((B == 5) or ( (E > 10) and (A < 8) )) 
#// (7) = 

print((((B == 5) or ((E > 10) and (A < 8))) or (A < B) or C) and C) 
#//(8) =
input("Appuyez sur Enter")