from werkzeug.security import generate_password_hash
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "static" / "annotations.jsonl"

# REGION_STATE_MAP = {
#     "East": ["West Bengal", "Arunachal Pradesh", "Assam", "Jharkhand", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Sikkim", "Tripura"],
#     "North": ["Uttar Pradesh", "Bihar", "Haryana", "Himachal Pradesh", "Punjab", "Rajasthan", "Uttarakhand", "Jammu and Kashmir", "Ladakh"],
# 	"Central": ["Madhya Pradesh", "Chhattisgarh"],
#     "South": ["Andhra Pradesh", "Telangana", "Karnataka", "Kerala", "Tamil Nadu"],
#     "West": ["Maharashtra", "Gujarat", "Goa"]
# }


# Sri Lankan provinces and their districts.
# Keep the existing variable name to avoid breaking other modules
# that import REGION_STATE_MAP.

REGION_STATE_MAP = {
    "Western": [
        "Colombo", "Gampaha", "Kalutara"
    ],
    "Central": [
        "Kandy", "Matale", "Nuwara Eliya"
    ],
    "Southern": [
        "Galle", "Matara", "Hambantota"
    ],
    "Northern": [
        "Jaffna", "Kilinochchi", "Mannar",
        "Mullaitivu", "Vavuniya"
    ],
    "Eastern": [
        "Ampara", "Batticaloa", "Trincomalee"
    ],
    "North Western": [
        "Kurunegala", "Puttalam"
    ],
    "North Central": [
        "Anuradhapura", "Polonnaruwa"
    ],
    "Uva": [
        "Badulla", "Monaragala"
    ],
    "Sabaragamuwa": [
        "Kegalle", "Ratnapura"
    ],
}

# Add only the actual Sri Lankan annotators who have been onboarded.
# Include "admin" only if the application expects it to appear here.
ONBOARDED_ANNOTATOR_USERNAMES = [
    "admin",
	"moana",
	"r1"
]

# Replace the example province with the admin's actual province.
# Add each annotator's province using the exact names in REGION_STATE_MAP.
ONBOARDED_ANNOTATOR_USERNAMES_STATES = {
    "admin": "Trincomalee",
	"moana": "Jaffna",
	"r1": "Nuwara Eliya"
}


# Update for pythonanywhere
# Update this list whenever new annotators are onboarded and should be highlighted in admin.
# ONBOARDED_ANNOTATOR_USERNAMES = [
# 	"admin",
# 	"Arnab6203",
# 	"nishtharajput",
# 	"Manasikelkar26",
# 	"Riddhi Vora",
# 	"Ajit Rana",
# 	"Priyanka",
# 	"Riddhi157",
# 	"tauseef",
# 	"Aishwarya Gadgil",
# 	"Ashish",
# 	"Manshi Patel",
# 	"Veera Hymavathi Sirisipalli",
# 	"Subham48",
# 	"Lila Ghimire",
# 	"neerav",
# 	"Sohail Khan",
# 	"Adya",
# 	"kameshwari04",
# 	"Manorath Thacker",
# 	"Payal",
# 	"hareeshreji",
# 	"Akhlaqur@12345",
# 	"binduhemant",
# 	"Gayathri",
# 	"Sylesh",
# 	"Som_Shikhar",
# 	"PallaviBeauvoir",
# 	"Palak_Shah",
# ]

# ONBOARDED_ANNOTATOR_USERNAMES_STATES = {
# 	"admin": "Uttar Pradesh",
# 	"Arnab6203": "West Bengal",
# 	"nishtharajput": "Haryana",
# 	"Manasikelkar26": "Maharashtra",
# 	"Riddhi Vora": "Gujarat",
# 	"Ajit Rana": "Haryana",
# 	"Priyanka": "Haryana",
# 	"Riddhi157": "Maharashtra",
# 	"tauseef": "Bihar",
# 	"Aishwarya Gadgil": "Maharashtra",
# 	"Ashish": "Jammu and Kashmir",
# 	"Manshi Patel": "Uttar Pradesh",
# 	"Veera Hymavathi Sirisipalli": "Andhra Pradesh",
# 	"Subham48": "West Bengal",
# 	"Lila Ghimire": "West Bengal",
# 	"neerav": "Uttar Pradesh",
# 	"Sohail Khan": "Jammu and Kashmir",
# 	"Adya": "Kerala",
# 	"kameshwari04": "Bihar",
# 	"Manorath Thacker": "Gujarat",
# 	"Payal": "Odisha",
# 	"hareeshreji": "Kerala",
# 	"Akhlaqur@12345": "Bihar",
# 	"binduhemant": "Andhra Pradesh",
# 	"Gayathri": "Andhra Pradesh",
# 	"Sylesh": "Andhra Pradesh",
# 	"Som_Shikhar": "Odisha",
# 	"PallaviBeauvoir": "Odisha",
# 	"Palak_Shah" : "Gujarat"
# }

HEGEMONY_AXES = [
	"social",
	"economic",
	"religious",	
	"gender",
	"linguistic",
	"colorism"
]

SHEET_NAME = "json-to-sheets-cultural-hegemony-annotation"

GOOGLE_CREDS_PATH = BASE_DIR / "accounts" / "google_creds.json"

API_KEYS_PATH = BASE_DIR / "accounts" / "apikeys.json"

with open(API_KEYS_PATH, "r") as f:
	KEYS = json.load(f)

# Model 3 uses the legacy `llama` key for GPT-OSS; Model 1 and 2 use
# explicit provider model names in the sheet while retaining legacy app keys.
HEADERS = [
	# --- metadata ---
	"id",
	"timestamp",
	"annotator_name",
	"region",
	"state",

	# --- prompts ---
	"base_prompt",
	"identity_prompt",

	# === LLAMA 4 MAVERICK BASE ===
	"llama4_maverick_base_output",
	"llama4_maverick_base_hallucination",
	"llama4_maverick_base_social",
	"llama4_maverick_base_social_impact",
	"llama4_maverick_base_economic",
	"llama4_maverick_base_economic_impact",
	"llama4_maverick_base_religious",
	"llama4_maverick_base_religious_impact",
	"llama4_maverick_base_gender",
	"llama4_maverick_base_gender_impact",
	"llama4_maverick_base_linguistic",
	"llama4_maverick_base_linguistic_impact",
	"llama4_maverick_base_colorism",
	"llama4_maverick_base_colorism_impact",

	# === GEMINI IDENTITY ===
	"llama4_maverick_identity_output",
	"llama4_maverick_identity_hallucination",
	"llama4_maverick_identity_social",
	"llama4_maverick_identity_social_impact",
	"llama4_maverick_identity_economic",
	"llama4_maverick_identity_economic_impact",
	"llama4_maverick_identity_religious",
	"llama4_maverick_identity_religious_impact",
	"llama4_maverick_identity_gender",
	"llama4_maverick_identity_gender_impact",
	"llama4_maverick_identity_linguistic",
	"llama4_maverick_identity_linguistic_impact",
	"llama4_maverick_identity_colorism",
	"llama4_maverick_identity_colorism_impact",

	# === GPT BASE ===
	# === QWEN3.8-27B BASE ===
	"qwen3_8_27b_base_output",
	"qwen3_8_27b_base_hallucination",
	"qwen3_8_27b_base_social",
	"qwen3_8_27b_base_social_impact",
	"qwen3_8_27b_base_economic",
	"qwen3_8_27b_base_economic_impact",
	"qwen3_8_27b_base_religious",
	"qwen3_8_27b_base_religious_impact",
	"qwen3_8_27b_base_gender",
	"qwen3_8_27b_base_gender_impact",
	"qwen3_8_27b_base_linguistic",
	"qwen3_8_27b_base_linguistic_impact",
	"qwen3_8_27b_base_colorism",
	"qwen3_8_27b_base_colorism_impact",

	# === GPT IDENTITY ===
	"qwen3_8_27b_identity_output",
	"qwen3_8_27b_identity_hallucination",
	"qwen3_8_27b_identity_social",
	"qwen3_8_27b_identity_social_impact",
	"qwen3_8_27b_identity_economic",
	"qwen3_8_27b_identity_economic_impact",
	"qwen3_8_27b_identity_religious",
	"qwen3_8_27b_identity_religious_impact",
	"qwen3_8_27b_identity_gender",
	"qwen3_8_27b_identity_gender_impact",
	"qwen3_8_27b_identity_linguistic",
	"qwen3_8_27b_identity_linguistic_impact",
	"qwen3_8_27b_identity_colorism",
	"qwen3_8_27b_identity_colorism_impact",

	# === LLAMA i.e GPT-OSS-120B BASE ===
	"llama_base_output",
	"llama_base_hallucination",
	"llama_base_social",
	"llama_base_social_impact",
	"llama_base_economic",
	"llama_base_economic_impact",
	"llama_base_religious",
	"llama_base_religious_impact",
	"llama_base_gender",
	"llama_base_gender_impact",
	"llama_base_linguistic",
	"llama_base_linguistic_impact",
	"llama_base_colorism",
	"llama_base_colorism_impact",

	# === LLAMA i.e GPT-OSS-120B IDENTITY ===
	"llama_identity_output",
	"llama_identity_hallucination",
	"llama_identity_social",
	"llama_identity_social_impact",
	"llama_identity_economic",
	"llama_identity_economic_impact",
	"llama_identity_religious",
	"llama_identity_religious_impact",
	"llama_identity_gender",
	"llama_identity_gender_impact",
	"llama_identity_linguistic",
	"llama_identity_linguistic_impact",
	"llama_identity_colorism",
	"llama_identity_colorism_impact",

	# === DEEPSEEK BASE ===
	"deepseek_base_output",
	"deepseek_base_hallucination",
	"deepseek_base_social",
	"deepseek_base_social_impact",
	"deepseek_base_economic",
	"deepseek_base_economic_impact",
	"deepseek_base_religious",
	"deepseek_base_religious_impact",
	"deepseek_base_gender",
	"deepseek_base_gender_impact",
	"deepseek_base_linguistic",
	"deepseek_base_linguistic_impact",
	"deepseek_base_colorism",
	"deepseek_base_colorism_impact",

	# === DEEPSEEK IDENTITY ===
	"deepseek_identity_output",
	"deepseek_identity_hallucination",
	"deepseek_identity_social",
	"deepseek_identity_social_impact",
	"deepseek_identity_economic",
	"deepseek_identity_economic_impact",
	"deepseek_identity_religious",
	"deepseek_identity_religious_impact",
	"deepseek_identity_gender",
	"deepseek_identity_gender_impact",
	"deepseek_identity_linguistic",
	"deepseek_identity_linguistic_impact",
	"deepseek_identity_colorism",
	"deepseek_identity_colorism_impact",

	"ground_truth",

	# --- references ---
	"references",
	"expert_reviews",
	"isAccept",
	"annotator_addressed",
]
