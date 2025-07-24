# converter_json_csv.py
import json
import pandas as pd

def convert_json_to_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        
        json_objects = [json.loads(line) for line in f if line.strip()]
        
    raw_texts = [obj.get("raw", "") for obj in json_objects]
    
    df = pd.DataFrame(raw_texts, columns=["Raw Text"])
    
    df.to_csv(output_file, index=False)
    print(f"✅ CSV created successfully: {output_file}")
