# adds new data to an old CSV file
import duckdb

conn = duckdb.connect()

conn.execute("CREATE TABLE life_expectancy AS SELECT * FROM read_csv_auto('life_expectancy.csv')")

conn.execute("""
    INSERT INTO life_expectancy VALUES ('Zanthera', 82.3, 78.9, 75.1);
INSERT INTO life_expectancy VALUES ('Drakonia', 85.7, 80.5, 75.8);
INSERT INTO life_expectancy VALUES ('Varkosia', 90.2, 88.4, 86.1);
INSERT INTO life_expectancy VALUES ('Lunara', 75.4, 70.8, 65.3);
INSERT INTO life_expectancy VALUES ('Neruvia', 68.1, 64.7, 61.2);
INSERT INTO life_expectancy VALUES ('Eldoria', 120.5, 110.3, 105.8);
INSERT INTO life_expectancy VALUES ('Morvex', 50.2, 48.5, 46.9);
INSERT INTO life_expectancy VALUES ('Xandria', 140.7, 135.2, 130.6);
INSERT INTO life_expectancy VALUES ('Quantara', 95.8, 92.1, 88.3);
INSERT INTO life_expectancy VALUES ('Oblivionia', 30.9, 28.5, 25.7);
""")

conn.execute("COPY life_expectancy TO 'updated_life_expectancy.csv' (HEADER, DELIMITER ',')")

print("CSV atualizado com sucesso!")

conn.close()