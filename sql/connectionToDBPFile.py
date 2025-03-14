import duckdb

# Conectar ao banco de dados exportado
conn = duckdb.connect("chessClubDB.dbp")

# Query para buscar os membros e suas escolas
query = """
SELECT 
    members.member_id, 
    members.name, 
    members.surname, 
    schools.school_name
FROM members
JOIN schools ON members.school_id = schools.school_id;
"""

# Executar a consulta e mostrar os resultados
df = conn.execute(query).fetchdf()
print(df)  # Ou use df.to_csv("output.csv") para salvar os resultados
