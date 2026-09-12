import re


def parse_resume(text):

    sections = {}

    headings = [
        "SUMMARY",
        "EDUCATION",
        "SKILLS",
        "CERTIFICATES",
        "LANGUAGES",
        "PROJECTS",
        "ACHIEVEMENTS"
    ]

    # Find all section headings
    heading_positions = []

    for heading in headings:

        pattern = rf"(?im)^\s*{re.escape(heading)}\s*$"

        match = re.search(pattern, text)

        if match:
            heading_positions.append(
                (match.start(), match.end(), heading)
            )

    # Arrange headings in the same order as they appear in the resume
    heading_positions.sort(key=lambda x: x[0])

    # Extract text between headings
    for i, (start, end, heading) in enumerate(heading_positions):

        if i + 1 < len(heading_positions):

            next_start = heading_positions[i + 1][0]

        else:

            next_start = len(text)

        content = text[end:next_start].strip()

        sections[heading.lower()] = content

    return sections