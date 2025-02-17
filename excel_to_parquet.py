import pandas

# Read the Excel file
df = pandas.read_excel('ColorFormats.xlsx')

# Write the Parquet file
df.to_parquet('ColorFormats.parquet')