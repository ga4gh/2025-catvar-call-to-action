import pandas as pd
import requests

request = "https://api.moalmanac.org/indications?organization=fda"
response = requests.get(url=request)
data = response.json()

records = []
for indication in data["data"]:
    record = {
        "application_number": indication["document"]["application_number"],
        "drug_name_brand": indication["document"]["drug_name_brand"],
        "drug_name_generic": indication["document"]["drug_name_generic"],
        "url": indication["document"]["url"],
        "indication": indication["indication"],
        "raw_biomarkers": (
            indication["raw_biomarkers"]
            if "raw_biomarkers" in indication.keys()
            else None
        ),
        "involves_categorical_variants": None,
        "categorical_variants": None,
    }
    records.append(record)
records = pd.DataFrame(records)
records.to_csv("fda_indications.raw.tsv", sep="\t", index=False)
