# -*- coding: utf-8 -*-
"""

"""

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import re
import pandas as pd

# Load model and tokenizer
model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16, trust_remote_code=True)

llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Build prompt (do not change)
def build_prompt(text):
    return f"""
    <think>
    A conversation between User and an intelligent information extraction assistant.
The assistant first thinks about the reasoning process and Rules in the mind and then provides the user with the extract structured advertisement details from raw OCR ad text.
Brand: The name of the company or platform responsible for promoting the advertisement.
- If the brand and advertiser differ (e.g., the platform is hosting but not promoting), prioritize the actual advertiser—the entity whose product or service is being marketed.
- Ignore platform names like Google, YouTube, Instagram, etc., unless they are the actual advertiser of the content.
- Focus on recognizable business or service names that the ad is trying to highlight or sell..
Product: The core offering, item, service, or experience that is being promoted in the advertisement.
- This could be a specific item (e.g., "Face Cream"), a service (e.g., "Matrimony App"), or a campaign (e.g., "Flat 50% Dining Offer").
- Avoid generic labels like "App" or "Website" unless the full product name is not discernible.
- Focus on the user benefit or feature the ad is promoting—what the user is expected to install, buy, or use.
- If multiple services are mentioned, prioritize the one most prominently associated with the brand.
Category: Type of content, e.g., Entertainment, E-commerce, Gaming, Education, etc.

reasoning:
1. First, let's understand what the question is asking
2. Break down the textual components
3. Apply relevant rules
4. Calculate step by step
5. Verify the result

Rules:
- Identify likely OCR-induced spelling errors using contextual clues, common word patterns, and known brand/product dictionaries.
- Prioritize text near 'Sponsored' or 'Visit site'
- Ignore brand names or product mentions that are not directly associated with "Sponsored", "Visit site", or ad-style call-to-actions.
- Do not confuse video/music content unless it's the ad product.
- Focus ONLY on content that is clearly sponsored or promotional in nature.
- Ignore personal content, unrelated hashtags, video titles, shorts, comments, timestamps,skip button like “advertiser”, “Skip”, “FREE”, “Google Play”, or any UI-related term in the brand.
- Ignore user handles (e.g., @name), search context, and Shorts UI text.
- Do not extract instructions or verbs as brand/product names.
- avoid generic or placeholder terms
- Do not confuse embedded videos or music tracks with ad products.
- Links to Facebook, YouTube, or redirect platforms aren’t necessarily the advertiser.
- Prefer the first sponsored item with a clear brand/product reference.
- If multiple brands are mentioned, choose the most prominent near “Sponsored”.
- Do NOT select common person names, generic words, or unrelated text as Brand.
- Only return clean, single-word brand names commonly known or appearing clearly alongside “Sponsored”, “Visit site”, or “Install”.
- If brand appears repeatedly, choose the first clean capitalized word after “Sponsored” or “Visit site”.
- Use categories like “Food Delivery”, “Photo Editing”, “Music Streaming”,"Health", "Finance", "Food & Beverage", "Tech", "App", "Gaming",
    "Education", "Entertainment", "Travel", "Real Estate", "E-commerce", "Streaming Services",
    "Home Appliances", "Beauty & Personal Care", "Insurance", "Investment" etc., instead of vague terms.

Extract the following fields **only** from the ad text below:

1. Brand
2. Product
3. Category

Format the output strictly in below format:
Brand: <brand name>
Product: <product name>
Category: <category name>

Do NOT explain or add any reasoning. Do NOT return anything except the three lines in the format shown.
</think>
Ad Text:
{text}

"""

# Predict + return response

def predict_ad(text):
    prompt = build_prompt(text)
    output = llm(prompt, do_sample=False, max_new_tokens=1000)[0]["generated_text"]
    return output[len(prompt):].strip()

def process_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["Extracted_Info"] = df["Raw Text"].apply(lambda x: predict_ad(str(x)))
    df.to_csv(output_csv, index=False)
    print(f" Output saved to: {output_csv}")
