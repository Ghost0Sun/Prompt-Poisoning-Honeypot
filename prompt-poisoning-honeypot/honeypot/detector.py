import re

def detect_malicious_prompt(prompt):
    patterns = [
        r"(ignore\s+previous\s+instructions)",
        r"(delete\s+.*\s+files)",
        r"(system\s+prompt)",
        r"(bypass\s+security)",
        r"(reveal\s+hidden\s+instructions)"
    ]
    for pattern in patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
    return False
