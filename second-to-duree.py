S = int(input("Entrer La duree en second : "))

A = S // 60
H = A // 60
M = A % 60
S = M // 60

print("La duree est", H , ":", M , ":" , S)
    
