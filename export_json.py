import json
import psycopg2

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

data = {}

TABLES = [
  'usa_state',
  'address',
  'accident'
]

if __name__ == '__main__':
    with conn:
        for i in TABLES:
            cur.execute('SELECT * FROM ' + i)
            rows = []
            fields = [x[0] for x in cur.description]
            for row in cur:
                rows.append(dict(zip(fields, row)))
            data[i] = rows

        with open('Ivanova_all.json', 'w') as json_out:
            json.dump(data, json_out, default=str)
