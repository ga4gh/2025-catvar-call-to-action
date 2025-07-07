# ClinVar
To characterize the expressions per Allele in ClinVar, we download the `hgvs4variation.txt.gz` output from ClinVar. More information can be found through [ClinVar's ftp README](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/README). Information on identifiers in ClinVar is [available through their documentation](https://www.ncbi.nlm.nih.gov/clinvar/docs/identifiers/).

This repository currently uses the version released on 2024-03-31 and last modified on 2025-06-30 (md5: d680fb3ffbee054a601785ba905c6a33). 

## Download data
To download from ClinVar and extract the file:

```bash
curl -O https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/hgvs4variation.txt.gz
curl -O https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/hgvs4variation.txt.gz.md5
gunzip -dk hgvs4variation.txt.gz
```