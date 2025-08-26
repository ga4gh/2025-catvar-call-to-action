import json
import pandas as pd


def load_json(file):
    with open(file) as fp:
        data = json.load(fp)
    return data


def write_json(data, file):
    json_object = json.dumps(data, indent=2)
    with open(file, "w") as outfile:
        outfile.write(json_object)


approvals_annotated = "fda_indications.annotated.tsv"
variants_annotated = "variant_categories.annotated.tsv"

output = "summary.json"

approvals = pd.read_csv(approvals_annotated, sep="\t", index_col=False)
approvals = approvals.loc[
    approvals["categorical_variants"].dropna().index, :
].reset_index(drop=True)
variants = pd.read_csv(variants_annotated, sep="\t", index_col=False)

approval_columns = [
    "application_number",
    "drug_name_brand",
    "drug_name_generic",
    "indication",
    "raw_biomarkers",
    "url",
    "categorical_variants",
]

records = []
for index in variants.index:
    series = variants.loc[index, :]
    variant = str(series.loc["entity"])

    relevant_approvals = approvals.loc[
        approvals["categorical_variants"].str.contains(variant, regex=False),
        approval_columns,
    ]
    relevant_approvals = relevant_approvals.to_dict("records")

    with pd.option_context("future.no_silent_downcasting", True):
        categories = (
            series.drop("entity").sort_index().fillna(value=False).to_dict()
        )

    record = {
        variant: {
            "categories": categories,
            "relevant_approvals": relevant_approvals,
            "relevant_approvals_count": len(relevant_approvals),
        }
    }
    records.append(record)

    print(
        f"{variant}: {pd.Series(categories)[pd.Series(categories)].shape[0]} categories and {len(relevant_approvals)} relevant approvals"
    )

write_json(data=records, file=output)
