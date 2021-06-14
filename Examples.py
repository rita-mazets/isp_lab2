import inspect

from ParserSerializer.Serializer import Serializer


base_value = 29
multiplier = 4


class Scholarship:
    name = "Lesha"

    def __init__(self, name):
        self.name = name
        self.coefficient = 1.4
        self.samples = ["Lesha", "gets", "a", "sholarship", "since", 1, "semester"]

    def base(self):
        return self.coefficient * multiplier


def difference(a, b):
    res = abs(a - b * base_value * multiplier)
    answer = f"Difference is {res}"
    return answer


def calculate(coeff):
    pers = Scholarship("Nastya")
    pers.coefficient = coeff
    total = pers.base()
    amount = base_value

    def multiplying_factor(coeff, amount):
        return coeff * amount

    compos = composite(multiplying_factor(total, amount))
    return difference(compos, pers.coefficient)


composite = lambda x: x * multiplier

person = Scholarship("Lesha")
person.coefficient = 1.6

json_seria = Serializer.create_serializer(".json")
pickle_seria = Serializer.create_serializer(".pickle")
toml_seria = Serializer.create_serializer(".toml")
yaml_seria = Serializer.create_serializer(".yaml")

met = yaml_seria.dump(calculate)
loaded = yaml_seria.load()
print(loaded(1.6))