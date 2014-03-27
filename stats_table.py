from stats_row import StatsRow

class StatsTable:
    def __init__(self, id, headers, stat_rows, career_row):
        self.table_name = id
        self.headers = headers
        self.stat_rows = self._make_stat_rows(stat_rows)
        self.career_row = self._make_stat_row(career_row)

    def __repr__(self):
        years = ' '.join(self.get_years())
        stats = ' '.join(self.headers)
        return "Table name: " + self.table_name + "\nYears: " + years + "\nStats: " + stats

    def __getattr__(self, attr):
        for header in self.headers:
            if header.lower() == attr.lower():
                return self.lookup_by_stat(header)

        raise AttributeError
    
    def lookup_by_stat(self, header):
        stats = {}
        for row in self.stat_rows:
            stats[row.season] = row.dict[header]
        return stats

    def get_years(self):
        years = []
        for row in self.stat_rows:
            years.append(row.season)
        return years

    def lookup_by_year(self, year):
        for row in self.stat_rows:
            if row.season == year:
                  return row

        return false

    def career(self):
        return self.career_row

    def _make_stat_rows(self, stat_rows):
        rows = []
        for stat_row in stat_rows:
            rows.append(self._make_stat_row(stat_row))
        return rows

    def _make_stat_row(self, row):
        return StatsRow(row, self)
