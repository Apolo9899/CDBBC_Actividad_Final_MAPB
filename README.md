# Analizador de ficheros SAM

Script de Python para analizar ficheros SAM y filtrar lecturas por calidad de mapeo (MAPQ), con pipeline Nextflow incluido.

## Descripción

Lee un fichero SAM línea a línea, ignora las cabeceras (`@`) y calcula cuántas lecturas superan un umbral de MAPQ indicado por el usuario. Los resultados se muestran en una tabla formateada en la terminal.

## Requisitos

- Python 3.8+
- Java 17+
- [uv](https://github.com/astral-sh/uv)
- [Nextflow](https://www.nextflow.io/)

## Instalación

```bash
# Instalar dependencias Python
uv sync

# Instalar Nextflow (requiere Java 17+)
curl -s https://get.nextflow.io | bash
sudo mv nextflow /usr/local/bin/
```

## Uso

### Opción 1: directamente con Python

```bash
uv run main.py <ruta_al_sam> <umbral_mapq>
```

Ejemplo:
```bash
uv run main.py Col0_C1.100k.sam 40
```

### Opción 2: pipeline Nextflow

```bash
nextflow run main.nf --sam <ruta_al_sam> --mapq <umbral_mapq>
```

Ejemplo:
```bash
nextflow run main.nf --sam Col0_C1.100k.sam --mapq 40
```

El parámetro `--mapq` es opcional, por defecto es 40.

## Ejemplo de salida

```
        Resultados del análisis SAM
┌──────────────────────────────────────┬──────────┐
│ Métrica                              │ Valor    │
├──────────────────────────────────────┼──────────┤
│ Lecturas totales                     │ 1500     │
│ Lecturas con MAPQ ≥ 40.0             │ 1350     │
│ Porcentaje de MAPQ superior al umbral│ 90.00%   │
└──────────────────────────────────────┴──────────┘
```

## Validaciones

El programa comprueba lo siguiente antes de ejecutarse:

- La ruta introducida existe
- El fichero tiene extensión `.sam`
- Si ninguna lectura supera el umbral, muestra un aviso

## Estructura del proyecto

```
proyecto-sam/
├── main.py        ← script Python de análisis
├── main.nf        ← pipeline Nextflow
├── pyproject.toml ← dependencias uv
├── uv.lock
└── README.md
```

## Dependencias

| Librería | Uso |
|---|---|
| `rich` | Formateo de la salida en terminal |

## Formato SAM

El formato SAM (Sequence Alignment Map) es un formato de texto para almacenar alineamientos de secuencias. Las líneas que empiezan por `@` son cabeceras y el resto son lecturas alineadas. La columna 5 (índice 4) contiene el valor MAPQ.
