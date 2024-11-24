from connect_settings import conn

cur = conn.cursor()

# Request to obtain the minimum and maximum age for names shorter than 6 characters.
query = """
SELECT MIN(age) AS min_age, MAX(age) AS max_age
FROM employees
WHERE LENGTH(name) < 6;
"""

cur.execute(query)
result = cur.fetchone()

# Result
print(f"Минимальный возраст: {result[0]}, Максимальный возраст: {result[1]}")

cur.close()
conn.close()
