import psycopg2
import matplotlib.pyplot as plt

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

query_1 = '''
-- 1. Визначити кількість інцидентів, що трапились в кожному із штатів
-- Вивести список у порядку спадання
CREATE VIEW States AS
SELECT usa_state, COUNT(zipcode) FROM USA_State
GROUP BY usa_state
ORDER BY COUNT(zipcode) DESC
'''

query_2 = '''
-- 2. Визначити кількість інцидентів однакового типу. 
-- Відсортувати за алфавітом.
CREATE VIEW SeverityStat AS
SELECT severity, COUNT(accident_id) FROM Accident
GROUP BY severity
ORDER BY severity ASC
'''

query_3 = '''
-- 3. Визначити кількість інцидентів в місяць
CREATE VIEW CountAccident AS
SELECT EXTRACT(MONTH FROM accident_date) AS MonthofDate, COUNT(accident_id)
FROM Accident
GROUP BY MonthofDate
ORDER BY MonthofDate ASC
'''

def query1():
    cur.execute('DROP VIEW IF EXISTS States')
    cur.execute(query_1)
    cur.execute('SELECT * FROM States')
    state = []
    accident = []
    for row in cur:
        state.append(row[0])
        accident.append(row[1])

    x_range = range(len(state))
    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(x_range, accident, label='Total')
    bar_ax.set_title('Кількість інцидентів, що трапились в кожному із штатів')
    bar_ax.set_xlabel('state')
    bar_ax.set_ylabel('number of accident')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(state)

    plt.bar(state, accident)
    plt.show()

def query2():
    cur.execute('DROP VIEW IF EXISTS SeverityStat')
    cur.execute(query_2)
    cur.execute('SELECT * FROM SeverityStat')
    severity = []
    accident = []
    for row in cur:
        word = row[0]
        severity.append(word[:25])
        accident.append(row[1])

    x, pie_ax = plt.subplots()
    pie_ax.pie(accident, labels=severity, autopct='%1.1f%%')
    pie_ax.set_title('Статистика різних типів інцидентів')
    plt.show()

def query3():
    cur.execute('DROP VIEW IF EXISTS CountAccident')
    cur.execute(query_3)
    cur.execute('SELECT * FROM CountAccident')
    month = []
    accident = []
    for row in cur:
        month.append(row[0])
        accident.append(row[1])
    x_range = range(len(month))
    figure, bar_ax = plt.subplots()
    bar_ax.set_title('Кількість інцидентів в різні місяці')
    bar_ax.set_xlabel('month')
    bar_ax.set_ylabel('number of accident')
    plt.bar(month, accident)
    plt.xticks(month, ['Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Oct', 'Nov'])
    plt.show()


if __name__ == '__main__':
    with conn:
        print("Database opened successfully")
        cur = conn.cursor()

        query1()
        query2()
        query3()
