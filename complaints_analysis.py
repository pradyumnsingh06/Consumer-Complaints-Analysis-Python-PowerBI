import pandas as pd

file_path = r'C:\Users\Pradyumn Singh\Desktop\Consumer_Complaints.csv'

print("Loading the dataset...")
df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
print("Dataset loaded successfully!")




print("\nCleaning all column names...")
df.columns = [col.lower().replace(' ', '_').replace('-', '_').replace('?', '') for col in df.columns]
print("Column names standardized.")

print("\nDropping unnecessary columns...")
columns_to_drop = ['tags', 'consumer_complaint', 'company_public_response', 'consumer_consent_provided', 'sub_product', 'sub_issue', 'zip_code']
df.drop(columns=columns_to_drop, inplace=True)
print("Columns dropped successfully!")

print("\nConverting date columns...")
df['date_received'] = pd.to_datetime(df['date_received'], format='mixed', errors='coerce')
df['date_sent_to_company'] = pd.to_datetime(df['date_sent_to_company'], format='mixed', errors='coerce')
print("Date columns converted successfully!")

print("\nCalculating response time...")
df['response_time'] = (df['date_sent_to_company'] - df['date_received']).dt.days
print("Response time calculated successfully!")

print("\nHandling missing values in 'state'...")
df['state'].fillna('Unknown', inplace=True)
print("Missing states filled.")

print("\nStandardizing text columns...")
df['state'] = df['state'].str.upper().str.strip()
df['company'] = df['company'].str.upper().str.strip()
print("Text columns standardized.")

print("\n--- Final Clean Data Summary ---")
# df.info()
print("\n--- Preview of Final Clean Data ---")
# print(df.head())
















# --- Part 3: Analysis & Visualization (Using Matplotlib Only) ---

# Import our plotting library
import matplotlib.pyplot as plt

# --- Analysis for Question 1: Geographical Hotspots ---

# 1. Find the top 15 states with the most complaints
print("Calculating the top 15 states with the most complaints...")
top_states = df['state'].value_counts().nlargest(15)
print(top_states)

# 2. Create a bar chart to visualize the top states using Matplotlib
print("\nCreating visualization...")
plt.figure(figsize=(12, 8)) # Set the size of the figure

# Create the horizontal bar chart
plt.barh(top_states.index, top_states.values, color='skyblue')

# Add a clear title and labels
plt.title('Top 15 States by Number of Consumer Complaints', fontsize=16)
plt.xlabel('Number of Complaints', fontsize=12)
plt.ylabel('State', fontsize=12)

# Invert the y-axis to show the highest value at the top
plt.gca().invert_yaxis()

# Display the final plot
# plt.show()



# --- Continuing Analysis for Question 1 ---

# 1. Define our list of top 5 states from the previous analysis
top_5_states = ['CA', 'FL', 'TX', 'NY', 'GA']

# 2. Filter our DataFrame to only include rows from these 5 states
df_top_states = df[df['state'].isin(top_5_states)]

# 3. Find the most common product complaints within this filtered data
top_products_in_top_states = df_top_states['product'].value_counts().nlargest(10)
print("Top 10 Product Complaints in the Busiest States:")
print(top_products_in_top_states)

# 4. Create a new bar chart to visualize this
print("\nCreating visualization...")
plt.figure(figsize=(12, 8))
plt.barh(top_products_in_top_states.index, top_products_in_top_states.values, color='teal')

# Add titles and labels
plt.title('Top 10 Product Complaints in CA, FL, TX, NY, & GA', fontsize=16)
plt.xlabel('Number of Complaints', fontsize=12)
plt.ylabel('Product Category', fontsize=12)
plt.gca().invert_yaxis() # Show highest at the top

# Display the plot
# plt.show()










# --- Analysis for Question 2: Corporate Accountability ---

# 1. Find the top 15 companies with the most complaints
print("Calculating the top 15 companies with the most complaints...")
top_companies = df['company'].value_counts().nlargest(15)
print(top_companies)

# 2. Create a bar chart to visualize the top companies
print("\nCreating visualization...")
plt.figure(figsize=(12, 8))
plt.barh(top_companies.index, top_companies.values, color='coral')

# Add titles and labels
plt.title('Top 15 Companies by Number of Consumer Complaints', fontsize=16)
plt.xlabel('Number of Complaints', fontsize=12)
plt.ylabel('Company', fontsize=12)
plt.gca().invert_yaxis() # Show highest at the top

# Display the plot
# plt.show()









# --- Continuing Analysis for Question 2 ---

# 1. Define our list of top 15 companies from the previous analysis
top_15_companies = top_companies.index.tolist()

# 2. Filter our DataFrame to only include rows from these 15 companies
df_top_companies = df[df['company'].isin(top_15_companies)]

# 3. Calculate the average response time for each of these companies
# We'll group by company and then find the mean of the 'response_time' column.
avg_response_time = df_top_companies.groupby('company')['response_time'].mean().sort_values()
print("Average Response Time (in days) for Top 15 Companies:")
print(avg_response_time)

# 4. Create a new bar chart to visualize this
print("\nCreating visualization...")
plt.figure(figsize=(12, 8))
plt.barh(avg_response_time.index, avg_response_time.values, color='purple')

# Add titles and labels
plt.title('Average Complaint Response Time for Top 15 Companies', fontsize=16)
plt.xlabel('Average Response Time (Days)', fontsize=12)
plt.ylabel('Company', fontsize=12)
plt.gca().invert_yaxis() # Show fastest at the top

# Display the plot
plt.show()




# --- Part 4: Export the Clean Data ---

print("\nSaving the clean data to a new CSV file...")
df.to_csv('complaints_cleaned.csv', index=False)
print("SUCCESS! Clean data saved to 'complaints_cleaned.csv'")