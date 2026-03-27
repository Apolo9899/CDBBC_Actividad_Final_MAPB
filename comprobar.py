import sys

RUTA_SAM= input("Introduce la ruta al sam")

with open(RUTA_SAM, "r") as fichero:
	for linea in fichero:
		if linea.startswith("@"):
			continue
		columnas = linea.strip().split("\t")
		MAPQ = columnas [4]
		print (MAPQ)	
