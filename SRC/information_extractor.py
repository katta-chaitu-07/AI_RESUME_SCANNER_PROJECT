import re


def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):

    pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_name(text):

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.upper() in ["RESUME", "CURRICULUM VITAE", "CV"]:
            continue

        return line

    return None


def extract_information(text):

    information = {}

    information["name"] = extract_name(text)
    information["email"] = extract_email(text)
    information["phone"] = extract_phone(text)

    return information