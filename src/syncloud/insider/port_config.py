import os.path
import convertible


class PortConfig:

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        items = convertible.read_json(self.filename)
        if not items:
            return []
        return items

    def save(self, items):
        convertible.write_json(self.filename, items)

    def add_or_update(self, mapping):
        if self.get(mapping.local_port):
            self.__update(mapping)
        else:
            self.__add(mapping)

    def __add(self, mapping):
        mappings_list = self.load()
        mappings_list.append(mapping)
        self.save(mappings_list)

    def remove(self, local_port):
        mappings_list = self.load()
        new_mappings = [m for m in mappings_list if m.local_port != local_port]
        self.save(new_mappings)

    def get(self, local_port):
        mappings_list = self.load()
        mapping = next((m for m in mappings_list if m.local_port == local_port), None)
        return mapping

    def __update(self, new_mapping):
        mappings_list = self.load()
        mapping = next((m for m in mappings_list if m.local_port == new_mapping.local_port), None)
        loc = mappings_list.index(mapping)
        mappings_list[loc] = new_mapping
        self.save(mappings_list)

    def remove_all(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)