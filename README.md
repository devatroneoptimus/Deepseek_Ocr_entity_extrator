# 🧠 Ad Information Extraction using DeepSeek-R1-Distill-Qwen-1.5B

This project extracts **Brand**, **Product**, and **Category** from raw OCR advertisement text using **LLM-based reasoning**. The pipeline uses the **DeepSeek-R1-Distill-Qwen-1.5B** model from Hugging Face for advanced reasoning and text understanding.

---

##  Features
✔ Handles **noisy OCR ad text** effectively  
✔ Extracts **Brand**, **Product**, and **Category** with custom rules  
✔ Processes **data from CSV** and outputs structured results    

---

##  Folder Structure
```
Deepseek_ocr_entity_extractor_project/
│
├── main.py                  # Main entry point
├── app.py                   # Model inference logic
├── converter_json_csv.py    # JSON → CSV converter
├── raw_text_batch.csv       # Intermediate file
├── ad_extraction_results.csv # Final output
├── requirements.txt


```
---

##  Technologies Used
- **Model:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`
- **Libraries:**  
  - `transformers` (Hugging Face)
  - `torch`
  - `pandas`
  

---

##  Installation
1. **Clone the repository**
   ```bash
   https://github.com/devatroneoptimus/Deepseek_Ocr_entity_extrator.git

### 2. ✅ Set up Python and Virtual Environment


```bash
python3 -m venv env
source env/bin/activate     # On Mac/Linux
env\Scripts\activate        # On Windows
```

---

### 3. ✅ Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Usage

1. **Prepare your input CSV**
   - Ensure your CSV file contains a column named `Raw Text` with OCR-extracted ad text.
   - Example:
     ```
     Raw Text
     "Emma Sleep India - Europe's best-selling mattress. Sponsored..."
     "Urbanrise World Of Joy 2 & 3 BHK Flats. Sponsored..."
     ```
---
### 5. ✅ Run the Application

```bash
python app.py
```

