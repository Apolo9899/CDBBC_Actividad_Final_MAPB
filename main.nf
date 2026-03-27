params.sam  = null
params.mapq = 40

if (params.sam == null) {
    error "Debes indicar un fichero SAM con --sam. Ejemplo: nextflow run main.nf --sam fichero.sam --mapq 40"
}

process analyze_sam {

    input:
    path sam_file

    output:
    stdout

    script:
    """
    uv run ${projectDir}/main.py ${sam_file} ${params.mapq}
    """
}

workflow {
    sam_ch = Channel.fromPath(params.sam)
    analyze_sam(sam_ch) | view
}
