import pandas as pd

data = {
    "Accident_Year": [2021, 2022, 2023],
    "Paid_12": [100000, 120000, 140000],
    "Paid_24": [130000, 150000, None],
    "Paid_36": [140000, None, None]
}

df = pd.DataFrame(data)

print(df)

df.to_excel(
    "actuarial_reserving_model.xlsx",
    index=False
)

print("Reserving dataset created.")