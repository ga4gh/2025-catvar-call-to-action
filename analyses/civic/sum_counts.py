import pandas as pd

input_file = "civic_variant_types.txt"
df = pd.read_csv(input_file, sep="\t")
variant_type_count = df["Name"].drop_duplicates().shape[0]
associated_variant_count = df["Count"].sum()
print(
    f"CIViC has curated {variant_type_count} and associated them with {associated_variant_count} variants."
)
