import psycopg2
import csv

# 1. Подключение к базе
conn = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="Qweasdzxc321s",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 2. Загрузка сотрудников (employees)
with open('employees_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        # row = [employee_id, first_name, last_name, title, birth_date, notes]
        cursor.execute(
            """INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )

# 3. Загрузка клиентов (customers)
with open('customers_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # row = [customer_id, company_name, contact_name]
        cursor.execute(
            "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

# 4. Загрузка заказов (orders)
with open('orders_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # row = [order_id, customer_id, employee_id, order_date, ship_city]
        cursor.execute(
            """INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) 
               VALUES (%s, %s, %s, %s, %s)""",
            (row[0], row[1], row[2], row[3], row[4])
        )

# 5. Сохраняем и закрываем
conn.commit()
cursor.close()
conn.close()
print("Все данные успешно загружены!")
