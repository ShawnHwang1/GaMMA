import pandas as pd
import glob

def convert_csv_to_pickdf(input_file, output_file):
    df = pd.read_csv(input_file)
    print("initial df")
    print(df)

    picks_df = pd.DataFrame(columns=["id", "timestamp", "prob", "type"])
    # Initialize counters and checks
    p_check = 0
    s_check = 0
    event_id = 0

    for index, row in df.iterrows():
        if (row['p_arrival_time'] != 0 and p_check == 0): # Check for p-arrival time
            picks_df = picks_df.append({
                "id": event_id,
                "timestamp": row["p_arrival_time"],
                "prob": row["p_probability"],
                "type": "p"
            }, ignore_index=True)
            p_check += 1
            event_id += 1
        elif (row['s_arrival_time'] != 0 and s_check == 0): # Check for s-arrival time
            picks_df = picks_df.append({
                "id": event_id,
                "timestamp": row["s_arrival_time"],
                "prob": row["s_probability"],
                "type": "s"
            }, ignore_index=True)
            s_check += 1
            event_id += 1

print(pick_df)