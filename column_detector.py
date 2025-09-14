import pandas as pd

def detect_column_types(df: pd.DataFrame, threshold: int = 20):
    column_types = {"numerical": [], "categorical": [], "text": []}
    
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            if df[col].nunique() < threshold:
                column_types["categorical"].append(col)
            else:
                column_types["numerical"].append(col)
        elif pd.api.types.is_string_dtype(df[col]):
            if df[col].nunique() < threshold:
                column_types["categorical"].append(col)
            else:
                column_types["text"].append(col)
        else:
            column_types["categorical"].append(col)
    
    return column_types


if __name__ == "__main__":
    data = {
        "Age": [25, 30, 22, 40],
        "Gender": ["M", "F", "M", "F"],
        "ZIP": [560001, 560002, 560001, 560003],
        "Bio": ["Loves coding", "Enjoys music", "Writes blogs", "Plays football"]
    }
    
    df = pd.DataFrame(data)
    print(detect_column_types(df))
