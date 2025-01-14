# COVID-19 Data Processing and Analysis System

## Project Overview
This project ingests, processes, and analyzes COVID-19 data to extract meaningful insights. The system is built using Python, PostgreSQL, and Pandas for data analysis.

## Design Decisions and Technologies Used

### Design Decisions:
1. Separation of Concerns: The project was divided into distinct scripts for data ingestion, processing, database setup, and analysis to ensure modularity and maintainability.
2. Data Transformation: Cleaning and reshaping the data was prioritized to ensure consistency and compatibility with the database schema.
3. Database Efficiency: PostgreSQL was chosen for its robust support for relational data and efficient querying capabilities, making it suitable for handling COVID-19 time-series data.
4. Scalability: The project structure and database schema were designed to allow easy extension to include additional data or analytical requirements.
5. Visualization: Matplotlib was used to generate clear and informative visualizations to present trends in the data.

### Technologies Used:
- Python: The primary programming language for data processing and analysis.
    - Pandas: Used for data manipulation and transformation.
    - Matplotlib: Used for visualizing data trends.
    - Seaborn: Used for creating advanced visualizations.
    - Psycopg2: Used to connect and interact with the PostgreSQL database.
- PostgreSQL: A robust relational database used for storing and querying COVID-19 data.
- pgAdmin: A graphical tool used for managing and exploring the PostgreSQL database.
- VS Code: The primary code editor used for development.
- CSV Files: Used to store processed data and analytical results.
- GitHub: Version control and project repository.

## How to Run the Project
1. Install the required Python libraries:

2. Run the scripts in the following order:
- `ingest_data.py`: Downloads the dataset.
- `process_data.py`: Cleans and processes the data.
- `setup_db.py`: Sets up the database and table.
- `insert_data.py`: Inserts the processed data into the database.
- Run queries under analysis folder.
    1. top5.py
    2. metrics_change.py
    3. metrics_change_graph.py
    4. focus_correlation.py
    5. extract_key_correlation.

## Data Analysis Results

### 1. Top 5 Countries with the Most Entries
The countries with the most rows in the dataset are:
- China: 38,862 entries
- Canada: 18,288 entries
- United Kingdom: 17,145 entries
- France: 13,716 entries
- Australia: 9,144 entries

### 2. Metric's Change Over Time: Daily Cases in the US
- Total cases in the US started at 1,829,340  on  2020-06-02.
- Cases doubled from 10 million to 20 million between 2020-11-08 and 2020-12-31.
- By the end of the dataset, total cases reached 103,802,702 as of 2023-03-09.

#### Visualization:

C:\Users\Jerome Espenida\Desktop\covid19-data-processing-system\daily_cases_us.jpg

## 3. Key Correlations Between Countries

### Analysis of Significant Correlations
The correlation analysis focused on COVID-19 case trends between selected countries. The findings highlight countries with strong similarities in case patterns over time.

### Top Correlations:
1. France and Italy: 0.997740
   - Both countries experienced similar pandemic waves, likely due to their geographic proximity and similar public health measures.
   
2. Canada and US: 0.996290
   - As neighbors with significant economic and social ties, their case trends are highly aligned.

3. Canada and Russia: 0.995828
   - Despite the geographic distance, aligned pandemic responses may explain this correlation.

4. Germany and Italy: 0.994652
   - European nations with synchronized pandemic measures and shared timelines.

5. Russia and US: 0.992326
   - Reflects potential alignment in global pandemic phases.

### Observations:
- Countries with high correlations often share geographic proximity, economic ties, or synchronized public health policies.
- Variations in correlations could stem from differences in pandemic timelines, reporting practices, or mitigation strategies.

### Recommendations:
- Investigate the causes of strong correlations between geographically distant countries (e.g., Canada and Russia).
- Analyze why certain countries, despite proximity, might show weaker correlations.
