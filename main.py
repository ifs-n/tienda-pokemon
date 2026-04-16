import os
os.system("cls")

pokeball = 1000
potion = 1500
revive = 3000
baya = 500
flag = True
acum_product = 0
quant_pokeball = 0
quant_potion = 0
quant_revive = 0
quant_baya = 0
try:
    print("------ Bienvenido  a PokeMarket ------")
    
    while flag == True:
        option = int(input("Seleccione un producto o termine su compra:\n1. Pokeball\n2. Poción\n3. Revivir\n4. Baya\n5. Finalizar Compra\n"))
        if option == 1:
            while quant_pokeball <= 0:
                quant_pokeball = int(input("Ingrese la cantidad deseada: "))
                if quant_pokeball > 0:
                    break
                else:
                    print("La cantidad no puede ser 0 o negativo")
            acum_product = acum_product + 1
            os.system("cls")
        elif option == 2:
            while quant_potion <= 0:
                quant_potion = int(input("Ingrese la cantidad deseada: "))
                if quant_potion > 0:
                    break
                else:
                    print("La cantidad no puede ser 0 o negativo")
            acum_product = acum_product + 1
            os.system("cls")
        elif option == 3:
            while quant_revive <= 0:
                quant_revive = int(input("Ingrese la cantidad deseada: "))
                if quant_revive > 0:
                    break
                else:
                    print("La cantidad no puede ser 0 o negativo")
            acum_product = acum_product + 1
            os.system("cls")
        elif option == 4:
            while quant_baya <= 0:
                quant_baya = int(input("Ingrese la cantidad deseada: "))
                if quant_baya > 0:
                    break
                else:
                    print("La cantidad no puede ser 0 o negativo")
            acum_product = acum_product = 0
            os.system("cls")
        elif option == 5 and acum_product > 0:
            flag = False
        else:
            print("El valor ingresado no es válido o no se ha comprado ningun producto")
    
    total_pokeball = pokeball * quant_pokeball
    total_potion = potion * quant_potion
    total_baya = baya * quant_baya
    total_revive = revive * quant_revive

    if quant_revive >= 3:
        revive_discount = total_revive * 0.15
    else:
        revive_discount = total_revive * 0

    revive_subtotal = total_revive - revive_discount
    
    total_partial = total_pokeball + total_potion + total_baya + total_revive
    total_withrevivedisc = total_pokeball + total_potion + total_baya + revive_subtotal
    
    total_product = quant_pokeball + quant_potion + quant_revive + quant_baya

    if total_product > 10:
        quant_discount = total_withrevivedisc * 0.05
    else:
        quant_discount = total_withrevivedisc * 0
    
    if total_partial > 5000:
        total_discount = total_withrevivedisc * 0.1
    else:
        total_discount = total_withrevivedisc * 0
    
    final_total = total_withrevivedisc - total_discount - quant_discount 
    
    discount = total_discount + quant_discount + revive_discount
    
    os.system("cls")
    print(f"Total bruto: {total_partial}\nTotal de descuentos: {discount}\nTotal a pagar: {final_total}\nCantidad de productos comprados: {total_product}\n")
    
except:
    print("malaso")