# US Food and Drug Administration
To characterize the number of oncology approvals by the US Food and Drug Administration, we reviewed fda approvals associated with a biomarker and categorized each as involving a broad class of genomic variation.

This analysis currently sources data from the [Molecular Oncology Almanac](https://dev.moalmanac.org), June 12th 2025 release. The following steps were performed to produce these results:
1. [Download and reformat data](#download-and-reformat-data)
2. [Annotate approvals for categorical variants](#annotate-approvals-for-categorical-variants)
3. [Extract categorical variants](#extract-categorical-variants)
4. [Annotate categorical variants for variant categories](#annotate-categorical-variants-for-variant-categories)
5. [Create summary file](#create-summary-file)
6. [Create visualization](#create-visualization)

From this data, I imagine a figure with categorical variant biomarkers along the rows, a comutation plot showing which axes the set defines specificity along (similiar to which constraint would be used), and then a horizontal bar chart of how many approvals relate to each biomarker.

## Download and reformat data
Regulatory approvals for oncology treatments from the [U.S. Food and Drug Administration](https://www.fda.gov/drugs/resources-information-approved-drugs/oncology-cancerhematologic-malignancies-approval-notifications) involving a biomarker were downloaded from the [Molecular Oncology Almanac](https://dev.moalmanac.org), June 12th 2025 release. These approvals were formatted into a tab delimited file, [fda_indications.raw.tsv](./fda_indications.raw.tsv), containing one approval per line with the following columns:
-  `application_number`: The source drug's US FDA application number.
- `drug_name_brand`: The brand name of the drug associated with the approval.
- `drug_name_generic`: The generic name of the drug associated with the approval.
- `indication`: The approval text from the US FDA.
- `url`: The url for the approval's drug's package insert which contains the approval.
- `raw_biomarkers`: The biomarker details as described in `indication`. Previously curated by the Molecular Oncology Almanac.
- `involves_categorical_variants`: None, a preallocated column.
- `categorical_variants`: None, a preallocated column.

```bash
python download.py
```

## Annotate approvals for categorical variants
The previously generated file of regulatory approvals, [fda_indications.raw.tsv](./fda_indications.raw.tsv), was copied to [fda_indications.annotated.tsv](./fda_indications.annotated.tsv). The latter file was manually reviewed to populate the `involves_categorical_variants` and `categorical_variants` columns, as follows:
- `involves_categorical_variants` (bool): A True or False label for if the approval cites a genomic variant with ambiguity (e.g., _BRAF_ V600 or t(_KMT2A_;v)), in contrast to a specific biomarker (e.g., _BRAF_ p.V600E or _BCR_::_ABL1_).
- `categorical_variants` (string): A formatted version of `raw_biomarkers` to group biomarkers cited. Multiple biomarkers per approval were delimited by a semicolon and space, `; `. For example, "deleterious or suspected deleterious BRCA-mutated (BRCAm)" was standardized to "(suspected) deleterious BRCA1 variants; (suspected) deleterious BRCA2 variants". 

## Extract categorical variants
Next, categorical variants were extracted from [fda_indications.annotated.tsv](./fda_indications.annotated.tsv) and written to a new file that places one per line, [variant_categories.raw.tsv](./variant-categories.raw.txt) using the script [extract_categorical_variants.py](./extract_categorical_variants.py). This script will additional print:
- The number of regulatory approvals involving a biomarker that cite a genomic variant with ambiguity.
- The above, as a fraction.
- The number of unique variant categories observed.

```bash
python extract_categorical_variants.py
```

## Annotate categorical variants for variant categories
The previously generated file of variant categories, [variant_categories.raw.tsv](./variant_categories.raw.tsv), was copied to [variant_categories.annotated.tsv](./variant_categories.raw.tsv). The latter file was then manually reviewed to add columns of variant categories that represent dimensions of categorical variation. Each column was populated with `TRUE` if the categorical variant listed in the `entity` column was  to that column's category. The following categories were identified from 44 reported variants:
- `allele_origin` - specifies an allele origin (germline or somatic).
- `amino_acid` - specifies 
- `clinical_annotation` - specifies variants of clinical relevance.
- `exon` - specifies an involved exon.
- `fusion_partner` - specifies one, but not both, involved genes for a fusion.
- `gene` - specifies an involved gene.
- `gene_set` - specifies a gene set. Note that the approval documents list genes that they consider to be members.
- `pathogenicity` - specifies a pathogenicity or likely pathogenicity requirement.
- `variant_type` - specifies the type of genomic variation (e.g., sequence variant, copy number alteration, rearrangement).

## Create summary file
Next, a json file was created to summarize findings to an output file called [summary.json](./summary.json), using both [fda_indications.annotated.tsv](./fda_indications.annotated.tsv) and [variant_categories.annotated.tsv](./variant_categories.annotated.txt). The top level of the file are categories of variation (the column `entity` from [variant_categories.annotated.tsv](./variant_categories.annotated.tsv)), with nested keys for `categories` (list), `approval_count` (integer), and `approvals` (list of dictionaries). 

```bash
python generate_summary.py
```

For example:
```json
[
  {
    "(suspected) deleterious BRCA1 variants": {
      "categories": {
        "allele_origin": false,
        "amino_acid": false,
        "clinical_annotation": false,
        "exon": false,
        "fusion_partner": false,
        "gene": true,
        "gene_set": false,
        "pathogenicity": true,
        "variant_type": false
      },
      "relevant_approvals": [
        {
          "application_number": 216793,
          "drug_name_brand": "Akeega",
          "drug_name_generic": "abiraterone acetate and niraparib",
          "indication": "AKEEGA is a combination of niraparib, a poly (ADP-ribose) polymerase (PARP) inhibitor, and abiraterone acetate, a CYP17 inhibitor indicated with prednisone for the treatment of adult patients with deleterious or suspected deleterious BRCA-mutated (BRCAm) metastatic castration-resistant prostate cancer (mCRPC). Select patients for therapy based on an FDA-approved test for AKEEGA.",
          "raw_biomarkers": "deleterious or suspected deleterious BRCA-mutated (BRCAm)",
          "url": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/216793s000lbl.pdf",
          "categorical_variants": "(suspected) deleterious BRCA1 variants; (suspected) deleterious BRCA2 variants"
        }
      ],
      "relevant_approvals_count": 1
    }
  },
...
]
```

## Create visualization
