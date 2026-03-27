import sys
import os
from rich.console import Console
from rich.table import Table

console = Console()

RUTA_SAM = sys.argv[1]
MAPQ_thr = float(sys.argv[2])

if not os.path.exists(RUTA_SAM):
    console.print(f"[bold red]ERROR:[/bold red] La ruta '{RUTA_SAM}' no existe")
    sys.exit(1)

if not RUTA_SAM.endswith(".sam"):
    console.print("[bold red]ERROR:[/bold red] El fichero introducido no es un archivo .sam")
    sys.exit(1)

with open(RUTA_SAM, "r") as fichero_sam:
    n_lecturas = 0
    n_MAPQ = 0

    for linea in fichero_sam:
        if linea.startswith("@"):
            continue

        columnas = linea.strip().split("\t")
        MAPQ = columnas[4]

        if int(MAPQ) >= MAPQ_thr:
            n_MAPQ += 1

        n_lecturas += 1

    if n_MAPQ == 0:
        console.print(f"[yellow]No hay ninguna lectura con MAPQ mayor de {MAPQ_thr}[/yellow]")

    # Mostrar resultados en una tabla
    tabla = Table(title="Resultados del análisis SAM")

    tabla.add_column("Métrica", style="cyan")
    tabla.add_column("Valor", style="green")

    tabla.add_row("Lecturas totales", str(n_lecturas))
    tabla.add_row(f"Lecturas con MAPQ ≥ {MAPQ_thr}", str(n_MAPQ))
    tabla.add_row("Porcentaje de MAPQ superior al umbral", f"{n_MAPQ * 100 / n_lecturas:.2f}%")

    console.print(tabla)
