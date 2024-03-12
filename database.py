from sqlalchemy import create_engine,text

engine = create_engine(
    "mysql+pymysql://admin:1234admin@database-1.c1i88wyoiw5h.eu-north-1.rds.amazonaws.com/gmembers?charset=utf8mb4"
)
with engine.connect() as conn:
  result = conn.execute(text("select * from trial"))
  print(result.all())