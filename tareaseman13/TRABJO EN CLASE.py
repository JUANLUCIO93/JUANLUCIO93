#crear un funsion para convertir grados centigrados a gardos fahrenheit
#fahrenheit =(9/5)*(grad_cent)+32
#kelvin=273.15+grad_cent

def conversion(tem_grad_cent):
    fahrenheit = (9/5) * (tem_grad_cent+32)
    kelvin = 273.15 + grad_cent

    return fahrenhit, kelvin

grad_cent = int(input ("ingrese gardos centigrados="))
fahrenhit,kelvin = conversion(grad_cent)

print("Grados fahrenhit:", fahrenhit)
print("Grados kelvin:", kelvin)

