import pandas as pd

def analyze_csv(filepath: str) -> str:
    try:
        # Read only the first 100 rows to save memory/tokens
        df = pd.read_csv(filepath).head(100)

        # Create a simple summary for the AI
        summary = (
            f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Columns are: {', '.join(df.columns.tolist())}. "
            f"Missing values: {df.isnull().sum().to_dict()}. "
            f"Basic statistics:\n{df.describe(include='all').to_string()}"
        )

        return summary

    except Exception as e:
        return f"Error processing CSV: {str(e)}"