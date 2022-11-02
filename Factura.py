print("Cantidad de productos en su canasta")
prods = int(input())
i=0
sub=0
while i<prods:
    print("Valor del producto ",i+1)
    val = int(input())
    print("Cantidad")
    cant = int(input())
    subpro=val*cant
    sub=sub+subpro
    i+=1
iva = sub * 0.19
total = sub + iva
print("Se vendieron: ",prods," Productos")
print("Subtotal: ",sub)
print("IVA 19% ",iva)
print("Total: ",total)