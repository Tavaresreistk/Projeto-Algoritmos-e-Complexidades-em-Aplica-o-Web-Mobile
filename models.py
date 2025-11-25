class Item:
    def __init__(self, name, category, quantity, code):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.code = code

warehouse_hash = {}

def add_to_hash(item):
    warehouse_hash[item.code] = item

def find_in_hash(code):
    return warehouse_hash.get(code, None)
