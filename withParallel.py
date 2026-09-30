import csv
import glob
import os
import time
from concurrent.futures import ProcessPoolExecutor
import kagglehub
import numpy as np
import pandas as pd


def process_chunk(temp_chunk):
    return (temp_chunk * 9 / 5) + 32


if __name__ == "__main__":
    print("1. Fetching dataset...")
    path = kagglehub.dataset_download("nachiketkamod/weather-dataset-us")


    csv_file = glob.glob(os.path.join(path, "*.csv"))[0]

    cols = pd.read_csv(csv_file, nrows=0).columns.tolist()
    target_col = next(
        (c for c in cols if str(c).strip().upper() in ["MAX", "TMAX"]), None
    )

    print(f"2. Loading 25k rows from '{target_col}'...")
    df = (
        pd.read_csv(csv_file, usecols=[target_col], nrows=25000)
        .replace(-999.9, np.nan)
        .dropna()
    )
    df[target_col] = df[target_col] / 10.0

    print("\n3. Processing in parallel...")
    start = time.time()

    num_workers = os.cpu_count() or 4
    chunks = np.array_split(df[target_col].to_numpy(), num_workers)

    processed_temps = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(process_chunk, chunks)
        for chunk_result in results:
            processed_temps.extend(chunk_result)

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
