def format_date(date):
    return date.strftime("%Y-%m-%d")

def parse_date(date_string):
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d")

def is_due(date):
    from datetime import datetime
    return date < datetime.now()