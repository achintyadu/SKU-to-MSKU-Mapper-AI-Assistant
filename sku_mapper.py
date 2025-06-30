import pandas as pd

# Step 1: Load Excel file and skip first 2 rows
mapping_file = 'WMS-04-02.xlsx'
mapping_df = pd.read_excel(mapping_file, skiprows=2)

# Step 2: Show available SKUs
print("\nAvailable SKUs:")
print(mapping_df['sku'].dropna().tolist())

# Step 3: Input SKU
sku_input = input("\nEnter SKU: ")

# Step 4: Match and display MSKU
matched_row = mapping_df[mapping_df['sku'] == sku_input]

if not matched_row.empty:
    print("MSKU is:", matched_row.iloc[0]['msku'])
else:
    print("No MSKU found for this SKU.")
