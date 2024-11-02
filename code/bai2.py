
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

# 2. Find top 3 highest and lowest values
def find_top_3(data, columns):
    for col in columns:
        if pd.api.types.is_numeric_dtype(data[col]): 
             # In 3 cầu thủ có giá trị cao nhất của chỉ số hiện tại
            print(f"Top 3 highest players for {col}:")
            print(data.nlargest(3, col)[['player', col]])
            print()
            
            # In 3 cầu thủ có giá trị thấp nhất của chỉ số hiện tại
            print(f"Top 3 lowest players for {col}:")
            print(data.nsmallest(3, col)[['player', col]])
            print("\n" + "-" * 50 + "\n") 
            
    

# 3. Calculate summary statistics and save
def calculate_statistics(data):
    tmp_df = data.copy()
    club_list = data['team'].unique().tolist()
    numeric_df = data.apply(pd.to_numeric, errors='coerce').drop(columns=['STT'], errors = 'ignore')
    summary_stats = pd.DataFrame() 
   
    overall_stats = {}            
    for col in numeric_df.columns:
        if not numeric_df[col].isnull().all():  
            overall_stats[f'{col}_Median'] = numeric_df[col].median()
            overall_stats[f'{col}_Mean'] = numeric_df[col].mean()
            overall_stats[f'{col}_Std'] = numeric_df[col].std()
    overall_stats_df = pd.DataFrame([overall_stats], index=["all"])
    summary_stats = pd.concat([summary_stats, overall_stats_df])

    
    col_to_convert = numeric_df.columns.difference(['team', 'STT'])
    numeric_df[col_to_convert] = numeric_df[col_to_convert].apply(pd.to_numeric, errors='coerce')
    for club in club_list:
        club_data = numeric_df[tmp_df['team'] == club]
        club_stats = {}
        for col in club_data.columns:
            if not club_data[col].isnull().all(): 
                club_stats[f'{col}_Median'] = club_data[col].median()
                club_stats[f'{col}_Mean'] = club_data[col].mean()
                club_stats[f'{col}_Std'] = club_data[col].std()
        
        if club_stats: 
            club_stats_df = pd.DataFrame([club_stats], index=[club])
            summary_stats = pd.concat([summary_stats, club_stats_df])
    summary_stats.to_csv('C:/Users/84976/Desktop/BTL_PTIT/PYTHON/btl/results2.csv', index_label="Team")


# 4. Plot histograms
def plot_histograms(data, columns):
    for col in columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            plt.figure()
            plt.hist(data[col].dropna(), bins=20, color='lightblue')
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

# 5. Calculate team performance
def calculate_team_performance(data):
    numeric_data = data.select_dtypes(include='number')
    numeric_data['Team'] = data['team']
    team_performance = numeric_data.groupby('Team').mean()
    overall_mean = team_performance.mean(axis=1)
    best_team = overall_mean.idxmax()
    return best_team



filepath = "C:/Users/84976/Desktop/BTL_PTIT/PYTHON/btl/results.csv" 
data = load_data(filepath)

columns = data.columns[3:] # loại bỏ col name, team, nation, position 

find_top_3(data, columns)

calculate_statistics(data)

   
#plot_histograms(data, columns)
    
best_team = calculate_team_performance(data)
print(f"Best performing team: {best_team}")
