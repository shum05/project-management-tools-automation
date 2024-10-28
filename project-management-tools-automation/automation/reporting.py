# Script to generate a report from collected data

import json
import pandas as pd

def load_data(filename='data/raw_data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def process_data(data):
    jira_df = pd.json_normalize(data['jira']['issues'])
    trello_df = pd.json_normalize(data['trello'])
    return jira_df, trello_df

def generate_report(jira_df, trello_df, output_file='data/processed_data.csv'):
    combined_df = pd.concat([jira_df, trello_df], axis=0)
    combined_df.to_csv(output_file, index=False)
    print(f"Report generated at {output_file}")

if __name__ == "__main__":
    data = load_data()
    jira_df, trello_df = process_data(data)
    generate_report(jira_df, trello_df)
