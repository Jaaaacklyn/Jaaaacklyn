

process fastqc {
    publishDir './results', mode: 'copy'   

    input:
    path fastq_file

    output:
    path "results/*_fastqc.html"
    path "results/*_fastqc.zip"

    script:
    """
    fastqc -o results $fastq_file
    """
}

// 定義流程的執行部分
workflow {
    fastq_files = Channel.fromFilePairs('/punim2383/fastq_data/ribo_minus/AGRF_CAGRF24030355_22KTLNLT3/*.fastq.gz')
    fastqc(fastq_files)
}
