dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

niveles_azucar = [130, 160, 95, 175, 160] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [115, 130, 110, 125, 175] # mmHg

print('RESULTADOS POR DIA: \n')
for i in range(5):
    print(f"{dias[i]}:")
    print(f'- Azucar: {niveles_azucar[i]} mg/dL')
    if niveles_azucar[i] > 70 and niveles_azucar[i] < 140:
        print('Dentro del rango normal.')
    else:
        print('ATENCIÓN: Niveles azucar fuera del rango normal.')
    print()
    print(f'- Consumo de sal: {niveles_sal[i]} mg/dia')    
    if niveles_sal[i] < 2300:
        print('Consumo normal de sal.')
    else:
        print('ATENCIÓN: Consumo de sal fuera del rango normal.')
    print()
    print(f'- Presión arterial: {presion[i]} mmHg')
    if presion[i] < 120:
        print('Presión normal')
    elif presion[i] >= 120 and presion[i] <= 129:
        print('ATENCION: Presion elevada.')
    elif presion[i] >= 130 and presion[i] <= 139: 
        print('ALERTA: Niveles de presión en el rango de hipertensión, etapa 1.')
    elif presion[i] >= 140: 
        print('ALERTA: Niveles de presión en el rango de hipertensión, etapa 2.')
    
    print()
    
print('RESULTADOS SEMANALES: ')
sum_azucar = 0
for i in niveles_azucar:
    sum_azucar += i
print(f'Promedio - azucar: {sum_azucar/len(niveles_azucar)} mg/dL')
sum_sal = 0
for i in niveles_sal:
    sum_azucar += i
print(f'Promedio - consumo de sal: {sum_azucar/len(niveles_azucar)} mg/dia')
sum_presion = 0
for i in presion:
    sum_azucar += i
print(f'Promedio - presion arterial: {sum_azucar/len(niveles_azucar)} mmHg')
