# Analizador de ficheros SAM

Script de Python para analizar ficheros SAM y filtrar lecturas por calidad de mapeo (MAPQ).

## Descripción

Lee un fichero SAM línea a línea, ignora las cabeceras (`@`) y calcula cuántas lecturas superan un umbral de MAPQ indicado por el usuario. Los resultados se muestran en una tabla formateada en la terminal.

## Requisitos

- Python 3.8+
- [uv](https://github.com/astral-sh/uv)

## Instalación

```bash
uv sync
```

## Uso

```bash
uv run main.py
```

El programa solicitará dos datos de forma interactiva:

1. **Ruta al fichero SAM** — ruta absoluta o relativa al fichero `.sam`
2. **Umbral de MAPQ** — valor numérico mínimo de calidad de mapeo

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

## Dependencias

| Librería | Uso |
|---|---|
| `rich` | Formateo de la salida en terminal |

## Formato SAM

El formato SAM (Sequence Alignment Map) es un formato de texto para almacenar alineamientos de secuencias. Las líneas que empiezan por `@` son cabeceras y el resto son lecturas alineadas. La columna 5 (índice 4) contiene el valor MAPQ.
