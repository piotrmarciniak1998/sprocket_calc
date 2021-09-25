from Value import Value


class Field:
    def __init__(self):
        self.name = "default_name"
        self.value = Value(0, 0)
        self.value_show = False
        self.description = "default_description"

    def __init__(self, name=str, px=int, mm=int, value_show=bool, description=str):
        self.name = name
        self.value = Value(px, mm)
        self.value_show = value_show
        self.description = description
