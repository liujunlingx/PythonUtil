# trim


class StringUtil:

    def trim(self,string):
        for index, elem in enumerate(string):
            if elem != ' ':
                start = index
                break

        for index, elem in enumerate(string[::-1]):
            if elem != ' ':
                end = len(string) - index
                break

        return string[start:end]


util = StringUtil()

# test trim function
print(util.trim(" hello"))
print(util.trim(" hello"))
print(util.trim("   hello"))
print(util.trim("hello "))
print(util.trim("hello    "))
print(util.trim(" hello "))
print(util.trim("    hello     "))
print(util.trim("   hello world   "))
