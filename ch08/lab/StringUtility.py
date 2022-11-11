class StringUtility:
    def __init__(self,string):
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        vowles = "a" or "e" or "i" or "o" or "u"
        vowleCount = 0
        if vowles in self.string:
            vowleCount += 1
            if vowleCount > 3:
                    return f"many"
    def bothEnds(self):

    def fixStart(self):

    def asciiSum(self):

    def cipher(self):
