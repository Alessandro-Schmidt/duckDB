# RetrieveData from an CSV file

import duckdb

duckdb.sql("CREATE TABLE life_expectancy AS SELECT * FROM read_csv_auto('updated_life_expectancy.csv')")

allResults = duckdb.sql('''
    SELECT "Country", "Sum of Life Expectancy  (both sexes)" 
    FROM life_expectancy
''')

print(allResults)