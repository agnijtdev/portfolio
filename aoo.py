mport os
import json
import gzip
import glob
import pandas as pd
from datetime import datetime
def load_grace71_events(datasets_dir="./hijack_events"):
"""Load confirmed hijack events from grace71 repo."""
    events = []
for fname in glob.glob(os.path.join(datasets_dir, "*.csv")):
        df = pd.read_csv(fname)
        events.append(df)
if not events:
return pd.DataFrame()
return pd.concat(events, ignore_index=True)
def load_tabi_hijacks(tabi_results_dir="./tabi_results"):
"""Load hijacks detected by tabi."""
    records = []
for fpath in glob.glob(os.path.join(tabi_results_dir,
"**", "all.hijacks.json.gz"),
                           recursive=True):
with gzip.open(fpath, "rt") as f:
for line in f:
try:
                    rec = json.loads(line)
                    records.append(rec)
except:
continue
return pd.DataFrame(records)
def merge_labels(parsed_data_dir="./parsed_data", output="./labeled_dataset.csv"):
"""
    Join parsed BGP records with hijack labels.
    Label = 1 if the announcement is part of a known hijack event.
    Label = 0 otherwise (normal).
    """
    grace_events = load_grace71_events()
    tabi_hijacks = load_tabi_hijacks()
print(f"Grace71 events: {len(grace_events)}")
print(f"Tabi detected: {len(tabi_hijacks)}")
# Load all parsed BGP records