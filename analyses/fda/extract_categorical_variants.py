import pandas as pd

input_file = "fda_indications.annotated.tsv"
output_file = "variant_categories.raw.tsv"
categorical_variant_delimiter = "; "

data = pd.read_csv(input_file, sep="\t", index_col=False)
relevant_data = data["categorical_variants"].dropna()
fraction = round(relevant_data.shape[0] / data.shape[0], 4)

records = []
for index in relevant_data.index:
    series = data.loc[index, :]
    variants = series.loc["categorical_variants"].split(categorical_variant_delimiter)  # type: ignore

    for variant in variants:
        records.append(variant)

unique = sorted(list(set(records)))
print(
    f"{len(relevant_data)} of {data.shape[0]} ({fraction * 100}%) oncology approvals involving a biomarker cited a genomic variant with ambiguity."
)
print(f"{len(unique)} unique variants categories were observed.")

(
    pd.Series(unique, name="entity").to_csv(
        "variant_categories.raw.tsv", sep="\t", index=False
    )
)
