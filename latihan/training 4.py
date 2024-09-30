print ("luas dan keliling lingkaran ")
print("------------------------------")

#rumus
r = float(input("masukan nilai jari-jari: "))
phi = 3.14
diameter = 2*r
luas = phi*r*r
keliling = phi*diameter
print ("_____________________")
#hasil
print ("\nluasnya     = ", str("%.2f" % luas))
print ("\nkelilingnya = ", str("%.2f" % keliling))