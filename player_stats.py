class PlayerStats:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

    def __getattr__(self, attr):
        for table in self.tables:
            if table.table_name.lower() == attr.lower():
                return table

        raise AttributeError

    def __repr__(self):
        return "Player: " + self.name + "\n" + "Stats tables: " + ' '.join(self.stats())

    def stats(self):
        table_names = []
        for table in self.tables:
            table_names.append(table.table_name)
        return table_names