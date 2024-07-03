from sqlalchemy import text
from sqlalchemy.orm import Session
from interface.connect_sqlite import ConnectionSQLite

# usando o contexto witj para imprimir uma frase
# with engine.connect() as conn:
#     result = conn.execute(text("select 'bom dia'"))
#     print(result.all())
engine = ConnectionSQLite().connection()

# inserindo valores em uma tabela e confirmandao a transação usando o commit

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (x INT, y INT)"))
    # inserindo dados
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 8},
             {"x": 7, "y": 10}
             ],
        
    )
    conn.commit()


sql = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(sql, {"y": 6})
    for row in result:
        print(row.x)



