class StatsRow:
    def __init__(self, row, table):
        self.row = row
        self.table = table
        self.headers = table.headers
        self.dict = self.make_row_dict()

    def __repr__(self):
        string = ""
        for key in self.dict:
            string += key + ": " + self.dict[key] + "\n"
        return string

    def __getattr__(self, name):
        header = self.case_agnostic_header_lookup(name)

        if header:
            return self.dict[header]
        else:
            raise AttributeError

    def case_agnostic_header_lookup(self, name):
        for header in self.headers:
            if name.lower() == header.lower():
                return header

        return False

    def make_row_dict(self):
        row_dict = dict(zip(self.headers, self.row))

        for key in row_dict.keys():
            if row_dict[key] == '':
                row_dict.pop(key)

        return row_dict