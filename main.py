import os
from converter_json_csv import convert_json_to_csv
from app import process_csv

if __name__ == "__main__":
    # File paths
    input_json = r"C:\Deepseek_Ocr_entity_extrator\input.json"   # Example: place your JSON in "input" folder
    intermediate_csv = "temp/raw_text_batch.csv"  # Temporary CSV
    output_csv = "results/ad_extraction_results.csv"  # Final CSV output

    #  Create necessary directories
    for path in [intermediate_csv, output_csv]:
        os.makedirs(os.path.dirname(path), exist_ok=True)

    print("Step 1: Converting JSON to CSV...")
    convert_json_to_csv(input_json, intermediate_csv)

    print("Step 2: Running LLM extraction on CSV...")
    process_csv(intermediate_csv, output_csv)

    print(f" Output saved to: {output_csv}")
