import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def visualize(df):
    """
    Automatically generates plots for each column in the DataFrame.
    """
    for col in df.columns:
        print(f"\nVisualizing: {col}")
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.figure(figsize=(12,4))
            
            plt.subplot(1, 3, 1)
            sns.histplot(df[col], kde=True)
            plt.title(f'Histogram of {col}')
            
            plt.subplot(1, 3, 2)
            sns.boxplot(y=df[col])
            plt.title(f'Boxplot of {col}')
            
            plt.subplot(1, 3, 3)
            if df.select_dtypes(include='number').shape[1] > 1:
                other_col = df.select_dtypes(include='number').columns[0]
                if other_col != col:
                    sns.scatterplot(x=df[col], y=df[other_col])
                    plt.title(f'Scatter Plot: {col} vs {other_col}')
            plt.tight_layout()
            plt.show()
        
        elif pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == 'object':
            plt.figure(figsize=(6,4))
            sns.countplot(x=df[col])
            plt.title(f'Count Plot of {col}')
            plt.xticks(rotation=45)
            plt.show()
        
        else:
            text_data = " ".join(df[col].astype(str).dropna())
            if text_data.strip() != "":
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
                plt.figure(figsize=(10,5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'Word Cloud of {col}')
                plt.show()
