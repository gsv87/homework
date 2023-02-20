import time


class Timer:
    def __init__(self):
        self.__start_time = 0
        self.__stop_time = 0

    def start(self):
        if self.__start_time == 0:
            self.__start_time = time.time()
        else:
            print('Timer уже запущен')

    def stop(self):
        if self.__start_time != 0 and self.__stop_time == 0:
            self.__stop_time = time.time()
        else:
            print('Timer не запущен')

    def reset(self):
        self.__start_time = 0
        self.__stop_time = 0

    def elapsed_time(self):
        if self.__start_time != 0:
            return round((time.time() if self.__stop_time == 0 else self.__stop_time) - self.__start_time, 2)
        print('Timer не запускался')
        return 0


class Phonebook:
    def __init__(self):
        self.__contact_list = {}

    def add_contact(self, name, phone_number):
        self.__contact_list[name] = phone_number

    def remove_contact(self, name):
        if name in self.__contact_list.keys():
            del self.__contact_list[name]
        else:
            print(f'Контакта с именем "{name}" нет')

    def update_contact(self, name, phone_number):
        self.add_contact(name, phone_number)

    def get_contact(self, name):
        if name in self.__contact_list.keys():
            return str(self.__contact_list[name])
        print(f'Контакт с именем {name} не найден')

    def get_all_contacts(self):
        return [(key, value) for key, value in self.__contact_list.items()]
