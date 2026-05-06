# [MSc Research Project: RNA-Seq Analysis Pipeline](https://jaaaacklyn.github.io/Jaaaacklyn/)

This project quantifies the differences between **Poly-A Selection** and **Ribo-Depletion** enrichment methods in RNA-Seq workflows.

### 🔬 Research Overview
*   **Objective**: To conduct a comparative analysis of RNA enrichment methods, focusing on their impact on data quality and downstream differential expression, particularly in clinical samples.
*   **Interactive Report**: [**View the Full Analysis Report & Visualizations**](https://jaaaacklyn.github.io/Jaaaacklyn/) (Hosted via GitHub Pages).

### 📁 Repository Structure
This project is organized to support reproducibility and clear data provenance:
*   `src/`: Core Nextflow pipeline scripts (e.g., `main.nf`, `fastqc.nf`).
*   `analysis/`: RMarkdown files for statistical modeling and thesis-specific analysis (`thesis_analysis.Rmd`).
*   `config/`: Configuration profiles and parameter files (`nextflow.config`, `params.json`).
*   `docs/`: Static HTML assets for the web-based research report.

### 🚀 Usage
The pipeline is built leveraging the **nf-core/rnaseq** framework.

**Basic Execution:**
```bash
nextflow run nf-core/rnaseq \
  --input <test.csv> \
  --outdir <output_directory> \
  --gtf <Homo_sapiens.GRCh38.113.gtf.gz> \
  --fasta <Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz> \
  -profile docker

### 🚀 How to Run
To reproduce the analysis using the local configuration, run the following command:
```bash
nextflow run nf-core/rnaseq -profile docker -params-file config/params.json -resume
