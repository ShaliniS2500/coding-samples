import os
import glob
import time
import multiprocessing
import pandas as pd
import numpy as np
import kagglehub


def process_raw_chunk(df_chunk, chunk_id, columns_to_use):
    df_chunk = pd.DataFrame(df_chunk, columns=columns_to_use)
    print(f"-> Computing Part {chunk_id}...")

    id_col = [c for c in df_chunk.columns if c.upper() == 'ID']
    max_col = [c for c in df_chunk.columns if c.upper() == 'MAX']

    res = df_chunk.groupby(id_col)[max_col].rolling(window=7, min_periods=1).mean()
    return len(res)


if __name__ == "__main__":
    print("--- PROGRAM 1: INSTANT LOAD & BENCHMARK ---")

    download_path = kagglehub.dataset_download("nachiketkamod/weather-dataset-us")
    csv_files = glob.glob(os.path.join(download_path, "*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in the downloaded directory.")

    target_csv = csv_files[0]

    print("Loading 15,000,000 rows from the 8.37GB file...")
    start_load = time.perf_counter()
    df_raw = pd.read_csv(target_csv, nrows=15_000_000)
    print(f"Loaded successfully in {time.perf_counter() - start_load:.2f} seconds!")

    df_raw.columns = df_raw.columns.str.strip()
    original_columns = list(df_raw.columns)

    print("\nExecuting Sequential Run...")
    chunks = np.array_split(df_raw, 3)
    start_seq = time.perf_counter()
    for idx, chunk in enumerate(chunks):
        process_raw_chunk(chunk, idx + 1, original_columns)
    seq_time = time.perf_counter() - start_seq
    print(f"Raw Sequential Timing: {seq_time:.4f} seconds")

    print("\nExecuting Parallel Run...")
    start_par = time.perf_counter()
    with multiprocessing.Pool(processes=3) as pool:
        args = [(chunk, idx + 1, original_columns) for idx, chunk in enumerate(chunks)]
        pool.starmap(process_raw_chunk, args)
    par_time = time.perf_counter() - start_par
    print(f"Raw Parallel Timing:   {par_time:.4f} seconds")
