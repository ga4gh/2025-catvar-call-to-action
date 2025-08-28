import pandas as pd

input_file = "Cosmic_Fusion_v102_GRCh38.tsv"
df = pd.read_csv(input_file, sep="\t", low_memory=False)

idx_5 = df[
    df["FIVE_PRIME_GENE_SYMBOL"].isin(["NTRK1", "NTRK2", "NTRK3"])
].index
idx_3 = df[
    df["THREE_PRIME_GENE_SYMBOL"].isin(["NTRK1", "NTRK2", "NTRK3"])
].index
idx = idx_5.union(idx_3)

# Some rows have several null values for `COSMIC_FUSION_ID` and `FUSION_SYNTAX`.
unique_ntrk_fusions = df.loc[
    idx, ["COSMIC_FUSION_ID", "FUSION_SYNTAX"]
].dropna()
for column in unique_ntrk_fusions.columns:
    print(unique_ntrk_fusions[column].unique().shape[0])
print("")

unique_fusion_strings = unique_ntrk_fusions["FUSION_SYNTAX"].unique()
unique_fusion_strings = pd.Series(unique_fusion_strings)
for NTRK in ["NTRK1", "NTRK2", "NTRK3"]:
    print(
        f"{NTRK}: {unique_fusion_strings.str.contains(NTRK).value_counts()[True]}"
    )
print("")

print("Unique COSMIC_FUSION_ID values for NTRK fusions:")
print("\n".join(unique_ntrk_fusions["COSMIC_FUSION_ID"].unique()))
print("")

print("Unique FUSION_SYNTAX values for NTRK fusions:")
print("\n".join(unique_ntrk_fusions["FUSION_SYNTAX"].unique()))
