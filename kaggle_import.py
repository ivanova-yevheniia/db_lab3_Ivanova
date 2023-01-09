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


query_1 = '''
CREATE TABLE usa_state_new(
    zipcode			    INT,
	usa_state		    CHAR(20) NOT NULL
)
'''

query_2 = '''
CREATE TABLE address_new(
	address_id		    CHAR(50) NOT NULL,
	zipcode			    INT,
	lat			    NUMERIC(9, 6),
	lng			    NUMERIC(9, 6),
	street			    CHAR(25) NULL,
	side			    CHAR(5) NULL
)
'''

query_3 = '''
CREATE TABLE accident_new(
	accident_id 		CHAR(10) NOT NULL,
	address_id		CHAR(50) NOT NULL,
	accident_date	        DATE,
	severity	        CHAR(50) NULL
)
'''

def query1():
    with open(r"C:\Users\yevhe\OneDrive\Desktop\Data Base\state.csv", 'r') as f1:
        cur.execute('DROP TABLE IF EXISTS usa_state_new')
        cur.execute(query_1)
        next(f1)
        cur.copy_from(f1, 'usa_state_new', sep=',')

def query2():
    with open(r"C:\Users\yevhe\OneDrive\Desktop\Data Base\address.csv", 'r') as f2:
        cur.execute('DROP TABLE IF EXISTS address_new')
        cur.execute(query_2)
        next(f2)
        cur.copy_from(f2, 'address_new', sep=',')


def query3():
    with open(r"C:\Users\yevhe\OneDrive\Desktop\Data Base\accident.csv", 'r') as f3:
        cur.execute('DROP TABLE IF EXISTS accident_new')
        cur.execute(query_3)
        next(f3)
        cur.copy_from(f3, 'accident_new', sep=',')



if __name__ == '__main__':
    with conn:
        print("Database opened successfully")

        query1()
        query2()
        query3()
        conn.commit()
