import kagglehub
import pandas as pd
import os

def load_data(path) -> pd.DataFrame: 
    # List files in the downloaded directory
    print("Downloaded files:", os.listdir(path))

    # Load the CSV file (adjust filename if needed)
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    if csv_files:
        df = pd.read_csv(os.path.join(path, csv_files[0]))
        print(f"\nLoaded {csv_files[0]}")
        print(f"Shape: {df.shape}")
        print(f"Shape: {df.columns}")

        print(f"\nFirst few rows:")
        print(df.head())
        return df 
    else:
        print("No CSV files found in the downloaded directory") 
        return None 



if __name__ == '__main__':
    # Download the dataset
    path = kagglehub.dataset_download("shreyashpatil217/netflix-trending-dataset")

    df = load_data(path)


    # Loaded Netflix_Data.csv
    # Shape: (8807, 12)
    # Shape: Index(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
    #     'release_year', 'rating', 'duration', 'listed_in', 'description'],
    #     dtype='object')

    for col in df.columns: 
        print(df[col].head())


    df_director_agg = df.groupby(['director', 'type']).agg(
        show_ct = ('show_id', 'count')    
    ).sort_values('show_ct', ascending = False)

    print(df_director_agg.head(20))
    

    # so who is rajiv chilaka 

    print(df[df['director'] == 'Rajiv Chilaka'].loc[:, ['title', 'description']])

    # looks like it's all the same series, indian animation, what happens if we redo agg with country 


    df_director_agg = df.groupby(['director', 'type', 'country']).agg(
        show_ct = ('show_id', 'count')    
    ).sort_values('show_ct', ascending = False)

    print(df_director_agg.head(20))


    # where did the rajiv go? 
    print(df[df['director'] == 'Rajiv Chilaka'].loc[:, ['title', 'description', 'country']])

    # doesn't properly get rid of india it seems. 


    df_director_agg = df[df['country'] == 'United States'].groupby(['director', 'type', 'country']).agg(
        show_ct = ('show_id', 'count')    
    ).sort_values('show_ct', ascending = False)

    print(df_director_agg.head(20))


    # are these all comedy specials? 
    print(df[df['director'] == 'Marcus Raboy'].loc[:, ['title', 'description', 'country', 'listed_in']])



    df_director_agg = df[df['country'] == 'United States'].groupby(['director', 'type', 'listed_in']).agg(
        show_ct = ('show_id', 'count')    
    ).sort_values('show_ct', ascending = False)

    print(df_director_agg.head(20))

