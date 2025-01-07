Quantifying the Differences Between Poly-A Selection and Ribo-Depletion in RNA-Seq

•	Overview of RNA-Seq and RNA Enrichment: Provide a brief discussion on RNA sequencing and the importance of RNA enrichment, particularly the necessity of rRNA depletion.

•	Research Gap: Highlight the lack of comprehensive, quantitative comparisons between Poly-A selection and Ribo-Depletion, with an emphasis on their impact on RNA-Seq data quality and downstream analyses.

•	Objective: Introduce the primary goal of the study, which is to conduct a detailed RNA-Seq analysis comparing these two RNA enrichment methods, with a particular focus on clinical samples.

nextflow run \nf-core/rnaseq \
    --input <polya_samplesheet.csv> \
    --outdir <OUTDIR> \
    --gtf <Homo_sapiens.GRCh38.113.gtf.gz> \
    --fasta <Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz> \
    -profile docker
    
nextflow run nf-core/rnaseq -profile docker -params-file params.json

