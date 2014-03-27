from table_ids import table_ids
from stats_table import StatsTable
from player_stats import PlayerStats

def find_header_row(table):
    rows = table.find_all('tr')
    for row in rows:
        if row['class'] == ['']:
            return row.find_all('th')

def find_stat_rows(table):
    rows = []
    for row in table.find_all(name='tr', class_='full_table'):
        row_cells = row.find_all('td')
        rows.append(row_cells)

    return rows

def find_career_stat_row(table):
    return table.find(class_='stat_total').find_all('td')

def get_row_contents(row):
    contents = []
    for cell in row:
        contents.append(cell.text.encode('ascii', 'ignore'))

    return contents

def get_headers(table):
    row = find_header_row(table)
    contents = get_row_contents(row)
    return contents

def get_stat_rows(table):
    stat_rows = find_stat_rows(table)
    rows = []
    for stat_row in stat_rows:
        contents = get_row_contents(stat_row)
        rows.append(contents)
    return rows

def get_career_stat_row(table):
    row = find_career_stat_row(table)
    contents = get_row_contents(row)
    return contents

def process_table(table):
    headers = get_headers(table)
    stat_rows = get_stat_rows(table)
    career_row = get_career_stat_row(table)
    id = table['id']
    table = StatsTable(id, headers, stat_rows, career_row)
    return table

def get_tables(stats_doc):
    tables = stats_doc.find_all('table', id=table_ids)
    return tables

def get_player_name(doc):
    return doc.h1.text

def make_player_stats(soup_doc):
    tables = get_tables(soup_doc)
    processed_tables = []
    for table in tables:
        processed = process_table(table)
        processed_tables.append(processed)

    name = get_player_name(soup_doc)
    stats = PlayerStats(name, processed_tables)
    return stats