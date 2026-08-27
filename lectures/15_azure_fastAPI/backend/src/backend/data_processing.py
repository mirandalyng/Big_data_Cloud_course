import pandas as pd
from backend.constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "Pokemon.csv")

df["Type 2"] = df["Type 2"].fillna("missing")
