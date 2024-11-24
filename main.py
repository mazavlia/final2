from .connect_settings import conn, cur

# Request to obtain the minimum and maximum age for names shorter than 6 characters.
query = """
SELECT MIN(age) AS min_age, MAX(age) AS max_age
FROM employees
WHERE LENGTH(name) < 6;
"""

cur.execute(query)
min_age, max_age = cur.fetchone()

# Result
print(f"Минимальный возраст: {min_age}, Максимальный возраст: {max_age}")

cur.close()
conn.close()
