def get_latest_pest(sheet):
    col = sheet.col_values(3)
    return (col[-1])

def get_latest_contact(sheet):
    col = sheet.col_values(4)
    return (col[-1])
