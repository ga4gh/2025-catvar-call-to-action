# US Food and Drug Administration
To characterize the number of oncology approvals by the US Food and Drug Administration, we reviewed fda approvals associated with a biomarker and categorized each as involving a broad class of genomic variation.

This analysis currently sources data from the [Molecular Oncology Almanac](https://dev.moalmanac.org), June 12th 2025 release.

From this data, I imagine a figure with categorical variant biomarkers along the rows, a comutation plot showing which axes the set defines specificity along (similiar to which constraint would be used), and then a horizontal bar chart of how many approvals relate to each biomarker.

## Download data
To download regulatory approvals from the FDA:
```bash
curl -O https://api.moalmanac.org/indications?organization=fda -o indications.json
```