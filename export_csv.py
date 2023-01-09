import psycopg2
import csv

username = 'student01'
password = 'postgress'
database = 'usa_accident'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(database=database,
                        host=host,
                        user=username,
                        password=password,
                        port=port)

cur = conn.cursor()

csv_out = 'Ivanova_DB_{}.csv'

TABLES = [
  'usa_state',
  'address',
  'accident'
]

if __name__ == '__main__':
    with conn:
        for i in TABLES:
            cur.execute('SELECT * FROM ' + i)
            fields = [x[0] for x in cur.description]
            with open(csv_out.format(i), 'w') as outfile:
                csv.writer(outfile).writerow(fields)
                for row in cur:
                    csv.writer(outfile).writerow([str(x) for x in row])
