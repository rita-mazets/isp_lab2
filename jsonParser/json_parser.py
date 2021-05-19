import inspect
import types
import json_utilities.json_utilities

sort_keys = False
f_found = {}


class Json:

    def loads(string):
        idx = 0
        try:
            while string[idx] == " " or string[idx] == "\n":
                idx += 1
        except IndexError:
            pass
        obj, idx = json_utilities.json_utilities.parse_symbol(string, idx)

        try:
            while True:
                if string[idx] != " " and string[idx] != "\n":
                    raise StopIteration(idx)
                idx += 1
        except IndexError:
            pass
        return obj

    def load(fp="testjson.json"):
        try:
            with open(fp, "r") as file:
                data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
        return Json.loads(data)

    def dumps(obj, indent=None, sort=False):
        global sort_keys
        sort_keys = sort
        if isinstance(indent, int) and indent > 0:
            step = " " * indent
            res = json_utilities.json_utilities._dumps(obj, step)
            if indent < 1:
                res = res.replace("\n", "")
        else:
            res = json_utilities.json_utilities._dumps(obj).replace("\n", "")
        return res

    def dump(obj, fp="testjson.json", indent=None, sort=False):
        string = Json.dumps(obj, indent, sort)
        try:
            with open(fp, "w") as file:
                file.write(string)
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
