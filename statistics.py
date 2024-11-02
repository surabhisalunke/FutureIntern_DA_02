
# Calculate mean, median, mode, and standard deviation for relevant numerical columns in the cleaned dataset
data_cleaned = pd.read_csv('cleaned_train.csv')
stats = {}

# Columns to analyze
columns = ["Age", "Fare", "SibSp", "Parch"]

for column in columns:
    stats[column] = {
        "mean": data_cleaned[column].mean(),
        "median": data_cleaned[column].median(),
        "mode": data_cleaned[column].mode()[0],  # mode() returns a Series; take the first mode if there's more than one
        "std_dev": data_cleaned[column].std(),
        
    }
    
stats
    


