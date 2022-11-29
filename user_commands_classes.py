from contact_book import AddressBook, Record, Iterable
from datetime import date
from abc import ABC, abstractmethod


address_book = AddressBook()


class UserCommands(ABC):

    @abstractmethod
    def command_to_execute(self):
        pass


class Greeting(UserCommands):

    def command_to_execute(self, *args) -> str:
        return 'How can I help you?'


class Exit(UserCommands):

    def command_to_execute(self, *args) -> str:
        address_book.save_address_book()
        return 'Good bye!'


class ContactBook(UserCommands):

    def command_to_execute(self, *args) -> list:
        return address_book.show_all_contacts()


class ShowByPages(UserCommands):
    
    def command_to_execute(self, args) -> str:
        result = Iterable(address_book, int(args[0]))
        for x in result:
            return str(x)
        

class NewContact(UserCommands):
    
    def command_to_execute(self, args: list) -> str:
        record = Record(args[0].capitalize())
        phone = int(args[1])
        record.add_new_phone(phone)
        return address_book.add_record(record)


class AddNewPhoneToContact(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        phone = int(args[1])
        return record.add_new_phone(phone)


class ChangeContact(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        existing_phone = int(args[1])
        new_phone = int(args[2])

        return record.change_phone(existing_phone, new_phone)


class GetPhoneNumberByName(UserCommands):
    
    def command_to_execute(self, args: list) -> list:
        record = address_book[args[0].capitalize()]
        return address_book.search_by_name(record)


class DeleteNumberFromContact(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        phone = int(args[1])
        return record.delete_phone(phone)


class SetupBirthday(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        birthday = date(year=int(args[1]), month=int(args[2]), day=int(args[3]))
        return record.set_birthday(birthday)
    

class ChangeBirthday(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        new_bday = date(year=int(args[1]), month=int(args[2]), day=int(args[3]))
        return record.change_birthday(new_bday)


class DaysToBirthday(UserCommands):

    def command_to_execute(self, args: list) -> str:
        record = address_book[args[0].capitalize()]
        return record.days_to_birthday()


class SaveAddressBook(UserCommands):

    def command_to_execute(self, *args) -> str:
        return address_book.save_address_book()


class LoadAddressBook(UserCommands):

    def command_to_execute(self, *args) -> str:
        return address_book.load_address_book()


class Find(UserCommands):

    def command_to_execute(self, args: list) -> str:
        return address_book.search_in_contact_book(args[0])


class Commands(UserCommands):

    def command_to_execute(self, *args) -> list:
        return [key for key in FUNCTIONS.keys()]


FUNCTIONS = {

    'hello' : Greeting, 
    'add' : NewContact, # + name + number
    'addnum': AddNewPhoneToContact, # + name + number
    'change' : ChangeContact, # + name + existing number + new number
    'phone' : GetPhoneNumberByName, # + name
    'delnum' : DeleteNumberFromContact, # name + number
    'show all' : ContactBook,
    'pages' : ShowByPages, # + number of pages
    'setbday' : SetupBirthday, # name + date(year, month, day)
    'correctbday' : ChangeBirthday, # name + new date (ear, month, day)
    'daysleft' : DaysToBirthday, # name
    'save' : SaveAddressBook,
    'load' : LoadAddressBook,
    'find' : Find, # find + letter or number
    'good bye' : Exit,
    'exit' : Exit,
    'close' : Exit,
    'commands' : Commands
}