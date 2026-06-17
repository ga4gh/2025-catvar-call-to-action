# A categorical variation call to action

This repository contains code for analyses pertaining to [The GA4GH Categorical Variation Representation Specification: A Unified Computational Framework for Reasoning over Genomic Variant Categories](https://www.biorxiv.org/content/10.64898/2026.02.10.705161). Here, we intend to provide a broad background of the presence of categorical variants within genomic knowledge bases. 

Supporting analyses include:
- [Variant types in CIViC](./analyses/civic/)
- [Multiple expressions per Allele ID in ClinVar](./analyses/clinvar/)
- [Counts of _NTRK_ fusions curated by COSMIC](./analyses/cosmic/)
- [FDA oncology approvals being indicated for categories of genomic variants](./analyses/fda/)

## Installation
### Download
This repository can be downloaded through GitHub by either using the website or terminal. To download on the website, navigate to the top of this page, click the green `Clone or download` button, and select `Download ZIP` to download this repository in a compressed format. To install using GitHub on terminal, type:

```bash
git clone ga4gh/2025-catvar-call-to-action
cd 2025-catvar-call-to-action
```

### Python dependencies
This repository uses Python 3.12. We recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and running Python with [conda-forge](https://conda-forge.org).

Run the following from this repository's directory to create a virtual environment and install dependencies with Anaconda or Miniconda:
```bash
conda create -y -n 2025-catvar-call-to-action python=3.12 -c conda-forge
conda activate 2025-catvar-call-to-action
pip install -r requirements.txt
```

Or, if using base Python: 
```bash
virtualenv venv
source activate venv/bin/activate
pip install -r requirements.txt
```

To make the virtual environment available to jupyter notebooks, execute the following code while the virtual environment is activated:
```bash
pip install jupyter
ipython kernel install --user --name=2025-catvar-call-to-action
```
