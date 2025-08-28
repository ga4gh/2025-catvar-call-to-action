# COSMIC fusions
As an illustrative example of the number of variants that can be associated with a categorical variant, we look at the number of _NTRK_ fusions curated by the [Catalog of Somatic Mutations in Cancer (COSMIC)](https://cancer.sanger.ac.uk/cosmic)'s [Gene Fusion Curation](https://cancer.sanger.ac.uk/cosmic/fusion). 

This analysis currently sources data from COSMIC version 102. The following steps were performed to produce our result:

1. [Download data](#download-data)
2. [Subset to _NTRK_ fusions](#subset-to-ntrk-fusions)

## Download data
COSMIC's gene fusion data for GRCh38 was downloaded [from their website](https://cancer.sanger.ac.uk/cosmic/download/cosmic/v102/fusion) through a non-commercial affiliation. The files were uncompressed and `Cosmic_Fusion_v102_GRCh38.tsv` was placed in this directory. This file was added to .gitignore, and needs to be individually downloaded to run code within this folder.

## Subset to _NTRK_ fusions
COSMIC's data as subsetted to _NTRK1/2/3_ fusions using the [count_curated_ntrk_fusions.py](./count_curated_ntrk_fusions.py) script by considering the `FIVE_PRIME_GENE_SYMBOL` and `THREE_PRIME_GENE_SYMBOL` columns. COSMIC includes several rows that contain null values for the columns `COSMIC_FUSION_ID` and `FUSION_SYNTAX`, and those were excluded. We observed that COSMIC has curated 26 distinct _NTRK_ fusions 
