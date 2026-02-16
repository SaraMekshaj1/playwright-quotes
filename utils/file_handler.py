import pandas as pd
from pathlib import Path

def save_to_csv(data, output_file, logger=None):
    Path("output").mkdir(exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

    if logger:
        logger.info(f"Saved {len(data)} rows to {output_file}")
