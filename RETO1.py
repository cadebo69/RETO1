'''
Un empleado de una de una empresa que se dedica a Call Center y tiene dudas de los descuentos que
le hacen por nómina, desea conocer cuánto dinero de descuentos tiene su sueldo exigidos por la ley
en relación con los pagos que la empresa le realizan mensualmente. Se ha firmado un contrato que
le permite trabajar 44 horas semanales. Con el propósito de verificar el valor total de los descuentos
han decidido construir un programa en Python que le permita verificar el valor de su salario antes
y después de realizar los descuentos. Después de consultar sobre la normatividad y revisar con detalle
su contrato laboral nota que debe tener en cuenta los siguientes aspectos:

El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 190.
Las horas extras se liquidan con un recargo del 34% sobre el valor de una hora normal.
Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 6.1% del salario base.
El salario total antes de descuentos se calcula como la suma del salario base, más el valor
de las horas extras, más las bonificaciones (si las hay).
Se descontará 1% del salario total antes de descuentos para el plan obligatorio de salud.
Se descontará 1% del salario total antes de descuentos para el aporte a pensión.
Se descontará 1% del salario total antes de descuentos para caja de compensación.

Luego de considerar toda esta información, el empleado decide construir un programa que permita
a cualquier empleado de la empresa verificar si los pagos son correctos.
'''
'''
pagoConDescuento = 0;
pagoSinDescuento = 0;
pagoTotal = 0;

salarioBase, horaExtra, bonoAdicional = input().split();
salarioBase = float(salarioBase);
horaExtra = int(horaExtra);
bonoAdicional = int(bonoAdicional);

horaNormal = salarioBase/190;
valorHoraExtra = (horaNormal * 1.34)*horaExtra;
valorBonoAdicional = ((salarioBase * 0.061)+salarioBase)*bonoAdicional;

pagoSinDescuento = salarioBase+valorHoraExtra+bonoAdicional;
pagoConDescuento = (pagoSinDescuento*0.03);
pagoTotal = pagoSinDescuento - pagoConDescuento

print (pagoSinDescuento);
print (pagoTotal);
'''

salarioBase, horaExtra, bonificacion = input().split();
salarioBase = float(salarioBase);
horaExtra = int(horaExtra);
bonificacion = int(bonificacion);

valorBonificacion = (bonificacion) * (salarioBase) * 0.061;

valorHora = (salarioBase) / 190;
valorHorasExtras = (valorHora*1.34)*(horaExtra);

salAntesDescuento = (salarioBase)+(valorHorasExtras)+(valorBonificacion);
totalDescuentos = (salAntesDescuento * 0.03);

SalDespuesDescuentos = salAntesDescuento - totalDescuentos;

print ("{0:.1f}".format(salAntesDescuento), "{0:.1f}".format(SalDespuesDescuentos));









