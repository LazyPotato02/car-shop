import mysql.connector


def init_connection():
    main_connection = mysql.connector.connect(
        host='10.70.71.106', database='emp_system', user='lazypotato', password='Password123#@!')
    return main_connection


def insert(credentials):
    connection = init_connection()

    cursor = connection.cursor()

    try:
        name = str(credentials[0])
        family = str(credentials[1])
        position = str(credentials[2])
        hour_salary = str(credentials[3])
        value = (name, family, position, hour_salary)
        sql = "INSERT INTO employees (name, family, position,hour_salary) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, value)

        connection.commit()
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return True


def list():
    connection = init_connection()

    cursor = connection.cursor()

    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM emp_system.employees;"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

        connection.commit()
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def remove():
    connection = init_connection()

    cursor = connection.cursor()

    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM emp_system.employees;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            print(x)

        input_string = tuple(input("Enter employee-id: "))
        sql = f"DELETE FROM employees where id = %s;"
        value = input_string
        cursor.execute(sql, value)

        connection.commit()
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return True


def update():
    connection = init_connection()

    cursor = connection.cursor()

    try:
        cursor = connection.cursor()
        input_string = input("Enter employee-id and position: ").split()
        emp_id = input_string[0]
        position = input_string[1]
        value = (position, emp_id,)
        sql = f"UPDATE employees SET position = (%s) WHERE id = (%s);"
        cursor.execute(sql, value)

        value = (emp_id,)
        sql = "SELECT * FROM emp_system.employees WHERE id = (%s);"
        cursor.execute(sql, value)
        result = cursor.fetchall()
        for x in result:
            print(x)

        connection.commit()

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return True
