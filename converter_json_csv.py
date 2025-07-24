import json
import pandas as pd

#  Input file path (update this with your local file path)
input_file = "/content/New Text Document.json" 

#  Output CSV path
output_file = "raw_text_batch.csv"

#  Read JSON lines from file
with open(input_file, "r", encoding="utf-8") as f:
    json_objects = [json.loads(line) for line in f if line.strip()]

#  Extract only the 'raw' text field
raw_texts = [obj.get("raw", "") for obj in json_objects]

#  Create a DataFrame
df = pd.DataFrame(raw_texts, columns=["Raw Text"])

#  Save to CSV
df.to_csv(output_file, index=False)

print(f" CSV created successfully: {output_file}")
print(df.head())  # Preview first few rows
