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









