import numpy as np
import json


class Interpreter:
    def __init__(self, program):
        self.program = program
        self.vars = {}
        self.output = []

    def get_keyword(self, row):
        if row[0] == 1:
            return "variable", row
        elif row[0] == 2:
            return "printing", row
        elif row[0] == 3:
            return "combine", row

    def tokenize(self):
        rsl = self.get_keyword(row=row)
        rsl_shortend = []
        # todo fix
        for element in rsl[1]:
            if element != 0:
                rsl_shortend.append(element)
            else:
                break
        print(rsl_shortend)
        values = np.array(rsl_shortend)
        searchval = 6
        all_seperators_pos = np.where(values == searchval)[0]
        if rsl[0] == "variable":
            self.vars[sum(rsl[1][all_seperators_pos[0]+1:all_seperators_pos[1]])] = sum(rsl_shortend[all_seperators_pos[1]+1:])
            return {"keyword": "var", "name": sum(rsl[1][all_seperators_pos[0]+1:all_seperators_pos[1]]), "value": sum(rsl_shortend[all_seperators_pos[1]+1:])}
        elif rsl[0] == "printing":
            if rsl[1][1] == 6 and rsl[1][2] == 6:
                if sum(rsl_shortend[3:]) in self.vars.keys():
                    self.output.append(self.vars[sum(rsl_shortend[3:])])
                    return {"keyword": "print", "value": self.vars[sum(rsl_shortend[3:])]}
                else:
                    return f"The variable: {sum(rsl_shortend[3:])} doen't exists!"
            else:
                self.output.append(sum(rsl_shortend[2:]))
                return {"keyword": "print", "value": sum(rsl_shortend[2:])}
        elif rsl[0] == "combine":
            if sum(rsl[1][all_seperators_pos[0]+1:all_seperators_pos[1]]) in self.vars.keys() and sum(rsl[1][all_seperators_pos[1]+1:all_seperators_pos[2]]) in self.vars.keys():
                var1 = self.vars.get(sum(rsl[1][all_seperators_pos[1]+1:all_seperators_pos[2]]))
                var2 = sum(rsl[1][all_seperators_pos[1]+1:all_seperators_pos[2]])
                self.vars[sum(rsl[1][all_seperators_pos[2]+1:])] = var1 + var2
                return {"keyword": "combined", "var_3_name": sum(rsl[1][all_seperators_pos[2]+1:]), "var3_value": var1 + var2}

    def run(self):
        for out in self.output:
            print(out)


if __name__ == "__main__":
    with open("painting.json", "r") as file:
        program = json.load(file)
    interpreter = Interpreter(program=program)
    for row in interpreter.program:
        if all(element == 0 for element in row):
            continue
        else:
            interpreter.tokenize()
            # print(interpreter.tokenize())
            # print(interpreter.output)
    interpreter.run()
