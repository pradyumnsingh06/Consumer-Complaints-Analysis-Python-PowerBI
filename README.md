Consumer Complaints Analysis (Python & Power BI)


Project Overview
This project is an end-to-end analysis of a large dataset containing over 1 million consumer complaints filed in the United States. The primary goal was to perform a complete data cleaning and preparation process using Python (Pandas) and then build an interactive two-page dashboard in Power BI to answer key business questions about corporate accountability and geographical trends in consumer grievances.

The analysis focuses on two core questions:

Geographical Hotspots: Which states generate the most complaints, and what are the primary issues in those regions?

Corporate Accountability: Which companies receive the most complaints, and how efficiently do they respond to them?

Dashboard Preview
Here is a preview of the final two-page interactive dashboard built in Power BI.

Page 1: Geographical Hotspots

Page 2: Corporate Accountability & Performance

The Python Data Cleaning Process
The raw dataset was extremely messy and required significant cleaning and transformation in Python before it could be used for analysis. The following steps were performed using the Pandas library:

Loaded & Inspected Data: Loaded a raw CSV file with over 1 million rows and identified significant issues, including messy column names, inconsistent date formats, and over 2.5 million missing data points across various columns.

Standardized Column Names: Converted all column names to a consistent "snake_case" format (e.g., Date received became date_received) to make them easier to work with in code.

Cleaned Date Columns: Converted text-based dates (date_received, date_sent_to_company) into proper datetime objects using pd.to_datetime with format='mixed' and errors='coerce' to handle multiple date formats and unparseable entries.

Feature Engineering: Created a new response_time column by calculating the number of days between date_received and date_sent_to_company. This new feature was a critical metric for analyzing corporate performance.

Handled Missing Data: Dropped unusable columns with excessive missing values (over 70% null). For key categorical columns like state, missing values were strategically filled with the placeholder "Unknown".

Standardized Text: Used .str.upper() and .str.strip() to standardize the state and company columns, ensuring accurate grouping and counting for the analysis.

Key Findings & Recommendations
Finding 1: Complaints are Concentrated in Populous States and the Financial Sector
Analysis: The dashboard clearly shows that the highest volume of complaints originates from the most populous states (California, Florida, Texas, New York). Within these states, the issues are overwhelmingly related to the financial services industry, with Mortgage, Debt Collection, and Credit Reporting being the top three complaint categories.

Recommendation: Consumer protection agencies in these key states should focus their resources on investigating practices within the financial services industry to address the root cause of these frequent complaints.

Finding 2: Complaint Volume Does Not Correlate with Response Speed
Analysis: The companies receiving the most complaints are the major credit bureaus (Equifax, etc.) and national banks. However, there is no clear correlation between the number of complaints a company receives and how quickly it responds.

Recommendation: Corporate accountability should be measured by a combination of complaint volume and response time. Companies with high complaint volumes but fast responses (like Equifax) may have efficient systems but underlying product issues, while companies with slow response times have clear operational inefficiencies that need to be addressed.

Tools Used
Python: For all data loading, cleaning, transformation, and initial analysis.

Pandas: For data manipulation and cleaning.

Matplotlib / Seaborn: For initial exploratory data visualization.

Power BI: For creating the final interactive dashboard and visualizations.
