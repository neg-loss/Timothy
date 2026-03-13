import re


def split_into_clauses(text):

    pattern = r"\n(?=\d+(\.\d+)*\s)"

    clauses = re.split(pattern, text)

    cleaned = [c.strip() for c in clauses if len(c.strip()) > 20]

    return cleaned