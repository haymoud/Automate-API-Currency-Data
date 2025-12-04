from api_fetcher import fetch_api_data, prepare_dataframe
from uploader import upload_to_gsheet

SHEET_ID = "19lpSWCeKGW5ymdg0Zvh9renvk4JoMLxtPW7H4Lx5sD4"

def run_pipeline():
    print("Fetching API data...")
    json_data = fetch_api_data()

    if not json_data:
        print("API request failed. Check logs.")
        return

    print("Preparing DataFrame...")
    df = prepare_dataframe(json_data)

    if df.empty:
        print("No valid data. Check logs.")
        return

    print("Uploading to Google Sheets...")
    upload_to_gsheet(df, SHEET_ID)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
