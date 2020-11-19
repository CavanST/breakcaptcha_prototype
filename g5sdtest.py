import string


class Cypher:
    def __init__(self):
        self.wheel = string.ascii_letters + ' ' + string.digits

    def show_alphabet(self):
        """
        Prints out the alphabet used for encrypting
        :return: The alphabet from init.
        """
        print('Using alphabet= ' + self.wheel)
        return 'a'

    def decrypt(self, input_string, key):
        """
        Decrypts the input
        :param: input_string: String to decrypt
        :param: key: The key to the cypher
        :return: A decrypted string
        """
        decrypted = ""
        wheel = list(my_cypher.wheel)
        for s in input_string:
            pos = wheel.index(s)
            new_pos = pos - key
            decrypted += wheel[new_pos]
        return decrypted


print('Decoding the string B0Vnjaor5m9V89q9gjk9mVdiVxt69mVzibdi99mdib....')
my_cypher = Cypher()
print(my_cypher.show_alphabet())
my_list = list(my_cypher.wheel)
for val in my_list:
    print("key: ", my_list.index(val))
    print(my_cypher.decrypt('B0Vnjaor5m9V89q9gjk9mVdiVxt69mVzibdi99mdib', my_list.index(val)))
