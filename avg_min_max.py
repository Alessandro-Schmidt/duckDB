# this file calculates the avarage, minimum and maximum life expectancy of the countries in the CSV file

import duckdb

duckdb.sql("CREATE TABLE life_expectancy AS SELECT * FROM read_csv_auto('updated_life_expectancy.csv')")

allResults = duckdb.sql('''
    SELECT
    AVG("Sum of Life Expectancy  (both sexes)") AS avg_life_expectancy, 
    MIN("Sum of Life Expectancy  (both sexes)") AS min_life_expectancy,
    MAX("Sum of Life Expectancy  (both sexes)") AS max_life_expectancy
    FROM life_expectancy;
''')

print(allResults)
duckdb.close()