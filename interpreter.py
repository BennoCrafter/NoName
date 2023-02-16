program = [1, 6, 3, 6, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class Interpreter:
    def __init__(self):
        self.program = [[1, 6, 3, 6, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_keyword(self):
        for row in self.program:
            if row[0] == 1:
                return "variable", row
            elif row[0] == 2:
                return "printing", row

    def tokenize(self):
        rsl = self.get_keyword()
        rls_shortend = []
        for element in rsl[1]:
            if element != 0:
                rls_shortend.append(element)
        print(rls_shortend)
        if rsl[0] == "variable":
            return {"keyword": "var", "name": rsl[1][2], "value": sum(rls_shortend[4:])}


if __name__ == "__main__":
    interpreter = Interpreter()
    print(interpreter.tokenize())