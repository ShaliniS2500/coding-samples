import csv
import glob
import os
import time
import kagglehub
import numpy as np
import pandas as pd


def process_temperature_sequentially(df, col_name):
    """Processes temperatures row-by-row sequentially."""
    results = []
    for idx, row_idx in enumerate(df.index):
        fahrenheit = (df.loc[row_idx, col_name] * 9 / 5) + 32
        results.append(fahrenheit)
        if (idx + 1) % 5000 == 0 or (idx + 1) == len(df):
            print(f" -> Processed {idx + 1}/{len(df)} temperatures...")
    return results


if __name__ == "__main__":
    print("1. Fetching dataset...")
    path = kagglehub.dataset_download("nachiketkamod/weather-dataset-us")

    # FIXED: Uses glob to safely pull the exact string path without lists
    csv_file = glob.glob(os.path.join(path, "*.csv"))[0]

    cols = pd.read_csv(csv_file, nrows=0).columns.tolist()
    target_col = next(
        (c for c in cols if str(c).strip().upper() in ["MAX", "TMAX"]), None
    )

    print(f"2. Loading 55k rows from '{target_col}'...")
    df = (
        pd.read_csv(csv_file, usecols=[target_col], nrows=55000)
        .replace(-999.9, np.nan)
        .dropna()
    )
    df[target_col] = df[target_col] / 10.0

    print("\n3. Processing sequentially...")
    start = time.time()
    processed_temps = process_temperature_sequentially(df, target_col)
    duration = time.time() - start

    print(f"\n4. Success! Duration: {duration:.4f} seconds")

    tracking_file = "performance_log.csv"
    file_exists = os.path.exists(tracking_file)
    with open(tracking_file, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                ["Entries Processed", "Columns Processed", "Duration (Seconds)"]
            )
        writer.writerow([len(df), 1, f"{duration:.4f}"])
