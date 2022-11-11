import string
class StringUtility:
    def __init__(self,string):
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        count = 0
        for letter in self.string:
            vowels = ["a","e","i","o","u"]
            if letter in vowels:
                count = count+ 1
        if count >= 5:
            return f"many"
        else:
            return f"{count}"
    def bothEnds(self):
        stringLength =len(self.string)
        if stringLength <= 2:
            return f""
        else:
            return f"{self.string[0]}{self.string[1]}{self.string[-2]}{self.string[-1]}"
    def fixStart(self):
        if len(self.string) <= 1:
            return self.string
        newString = ""
        firstLetter = self.string[0]
        check = False
        for letter in self.string:
            if letter != firstLetter:
                newString += letter
            else:
                if check ==True:
                    newString += "*"
                else:
                    newString +=letter
                    check = True
        return newString
    def asciiSum(self):
        aciisum = 0
        for letter in self.string:
            aciisum += ord(letter)
        return aciisum
    def cipher(self):
        alphabet = list(string.ascii_letters)
        length =len(self.string)
        print(alphabet)
        newString=""
        for letter in self.string:
            check = False
            for c in alphabet:
                if letter == c:
                    check =True
                    num = c.index
                    newNum = num +length
                    if newNum > 25:
                        newNum = 26
                    newString += alphabet[newNum]
            if check == False:
                for c in alphabet:
                    if letter == c:
                        check ==True
                        num =alphabet.index(c)
                        newNum = num + length
                        if newNum >25:
                            newNum -= 26
                        newString +=alphabet[newNum]
            return newString





