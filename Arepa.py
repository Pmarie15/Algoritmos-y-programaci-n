def calcular_volumen_ingredientes(agua_tzas, harina_tzas, sal_cdtas, aceite_cdas):

    if any(cant < 0 for cant in [agua_tzas, harina_tzas, sal_cdtas, aceite_cdas]):
        return None
    cda_a_cc = 14.79
    cdta_a_cc = 4.93
    tza_a_cc = 236.59

    volumen_agua = agua_tzas * tza_a_cc
    volumen_harina = harina_tzas * tza_a_cc
    volumen_sal = sal_cdtas * cdta_a_cc
    volumen_aceite = aceite_cdas * cda_a_cc

    volumen_total = volumen_agua + volumen_harina + volumen_sal + volumen_aceite

    volumen_final = volumen_total * 0.90  

    return volumen_final

def obtener_cantidades():
    while True:
        try:
            agua_tzas = float(input("Ingrese la cantidad de agua en tazas: "))
            harina_tzas = float(input("Ingrese la cantidad de harina en tazas: "))
            sal_cdtas = float(input("Ingrese la cantidad de sal en cucharaditas: "))
            aceite_cdas = float(input("Ingrese la cantidad de aceite en cucharadas: "))
            return agua_tzas, harina_tzas, sal_cdtas, aceite_cdas
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

def main():
    
    agua_tzas, harina_tzas, sal_cdtas, aceite_cdas = obtener_cantidades()

    volumen_ingredientes = calcular_volumen_ingredientes(agua_tzas, harina_tzas, sal_cdtas, aceite_cdas)

    if volumen_ingredientes is None:
        print("Por favor, ingrese valores positivos para las cantidades de ingredientes.")
    else:
        print(f"El volumen de la arepa cocida (considerando la evaporación) es: {volumen_ingredientes:.2f} cc")

if __name__ == "__main__":
    main()