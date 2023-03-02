#paso1: pedirle al usuario los ingresos
ingresos = float(input("Por favor digite los ingresos de la empresa: "))
#paso2: pedirle al usuario los costos
costos = float(input("Por favor digite los costos de la empresa: "))
#paso3: calcular la utilidad bruta (ingresos-costos)
utilidadBruta = ingresos - costos
#paso4: pedirle al usuario los gastos
gastos = float(input("Por favor ingrese los gastos de la empresa: "))
#paso5: calcular la utilidad operativa (utilidad bruta-gastos)
utilidadOperativa = utilidadBruta - gastos
#paso6: calcular el impuesto a la renta (utilidad operativa * 30%)
impuestoRenta = utilidadOperativa * 0.3
#paso7: calcular la utilidad neta (utilidad bruta - impuesto a la renta)
utilidadNeta = utilidadBruta - impuestoRenta

print(f"La utilidad bruta de la empresa es: {utilidadBruta}")
print(f"La utilidad operativa de la empresa es: {utilidadOperativa}")
print(f"El total de los impuestos de renta de la empresa es: {impuestoRenta}")
print(f"La utilidad neta de la empresa es: {utilidadNeta}")
