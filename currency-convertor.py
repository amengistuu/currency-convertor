# RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
# ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
# HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
# AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
# MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.

currencies = {
    "RUB": 2.98,
    "ARS": 0.82,
    "HNL": 0.17,
    "AUD": 1.9622,
    "MAD": 0.208
}

# Get the number of conicoins from user input.
conicoin = float(input())
# Print how much you will get in all five currencies mentioned above.
print(f'I will get {conicoin * currencies["RUB"]} RUB from the sale of {conicoin} conicoins.')
print(f'I will get {conicoin * currencies["ARS"]} ARS from the sale of {conicoin} conicoins.')
print(f'I will get {conicoin * currencies["HNL"]} HNL from the sale of {conicoin} conicoins.')
print(f'I will get {conicoin * currencies["AUD"]} AUD from the sale of {conicoin} conicoins.')
print(f'I will get {conicoin * currencies["MAD"]} MAD from the sale of {conicoin} conicoins.')