# this file calculates the avarage, minimum and maximum life expectancy of the countries in the CSV file

import duckdb

duckdb.sql("CREATE TABLE life_expectancy AS SELECT * FROM read_csv_auto('updated_life_expectancy.csv')")

allResults = duckdb.sql('''
    
    SELECT 
    AVG("Sum of Life Expectancy  (both sexes)") AS avg_life_expectancy,
    MIN("Sum of Life Expectancy  (both sexes)") AS min_life_expectancy_value,
    (SELECT Country FROM life_expectancy ORDER BY "Sum of Life Expectancy  (both sexes)" ASC LIMIT 1) AS country_with_min,
    MAX("Sum of Life Expectancy  (both sexes)") AS max_life_expectancy_value,
    (SELECT Country FROM life_expectancy ORDER BY "Sum of Life Expectancy  (both sexes)" DESC LIMIT 1) AS country_with_max
FROM life_expectancy
    
''')

print(allResults)

duckdb.close()