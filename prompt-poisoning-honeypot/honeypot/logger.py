import pandas as pd
from datetime import datetime
import os

LOG_FILE = "data/attacks_log.csv"

def log_attack(ip, prompt):
    new_entry = pd.DataFrame([{
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "prompt": prompt
    }])
    
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry
    
    df.to_csv(LOG_FILE, index=False)
