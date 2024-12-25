import psycopg2

# 数据库连接信息
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
# 设置 search_path 
cur.execute("SET search_path TO raw_cdc;")
import os
# 设置 CSV 文件目录
csv_directory = "csv/"

def load_csv_to_postgres(csv_file, table_name):
    with open(csv_file, 'r') as f:
        cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ','", f)
    conn.commit()

# 遍历目录中的所有 CSV 文件并加载到对应的表中
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        csv_file = os.path.join(csv_directory, filename)
        table_name = os.path.splitext(filename)[0]  # 文件名去掉扩展名作为表名
        print(f"Loading {csv_file} into table {table_name}...")
        load_csv_to_postgres(csv_file, table_name)
        print(f"Loaded {csv_file} into table {table_name} successfully!")
# 关闭游标和连接
cur.close()
conn.close()
