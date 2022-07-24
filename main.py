from mysql_worker import insert, list, remove, update


class CreateEmployee:

    def __init__(self, name, family_name, position, hour_salary):
        self.name = name
        self.family_name = family_name
        self.position = position
        self.hour_salary = str(hour_salary)

    def insert_value(self):
        value_to_return = self.name, self.family_name, self.position, self.hour_salary
        is_completed = insert(value_to_return)
        if is_completed:
            return 'Worker Successfully Added!'
        return 'Worker cannot be added!'


class ListEmployee:
    @staticmethod
    def show_employees():
        result = list()
        for x in result:
            print(x)


class RemoveEmployee:
    @staticmethod
    def remove_employee():
        is_completed = remove()
        if is_completed:
            return 'Worker removed Successfully!'
        return 'Worker not found!'


class UpdateEmployee:
    @staticmethod
    def update_employee():
        is_completed = update()
        if is_completed:
            return 'Worker Successfully updated!'
        return 'Worker not found!'


def main():
    val = input("-(insert)\n-(list)\n-(remove)\n-(update)\n Enter mysql command => ")

    if val == 'insert':
        input_line = input('Enter Employee information (name) (family) (position): ').split()
        w = CreateEmployee(input_line[0], input_line[1], input_line[2], 46.50)
        w.insert_value()
    elif val == 'list':
        lw = ListEmployee
        lw.show_employees()
    elif val == 'remove':
        rmw = RemoveEmployee
        rmw.remove_employee()
    elif val == 'update':
        upd = UpdateEmployee
        upd.update_employee()
    elif val == 'exit':
        exit()


while __name__ == '__main__':
    main()
