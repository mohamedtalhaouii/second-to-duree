S = int(input("Entrer La duree en second : "))

H = S // 3600
A = S % 3600
M = A // 60
S = A % 60

print("La duree est", H , "h :", M , "m :" , S, "s")
    
