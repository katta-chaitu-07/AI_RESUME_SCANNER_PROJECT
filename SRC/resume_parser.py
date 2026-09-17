import re


def parse_resume(text):

    sections = {}

    # Resume section headings we want to detect
    headings = [
        "SUMMARY",
        "EDUCATION",
        "SKILLS",
        "CERTIFICATES",
        "LANGUAGES",
        "PROJECTS",
        "ACHIEVEMENTS"
    ]

    # Store the position of every heading found in the resume
    heading_positions = []

    for heading in headings:

        pattern = rf"(?im)^\s*{re.escape(heading)}\s*$"

        match = re.search(pattern, text)

        if match:
            heading_positions.append(
                (match.start(), match.end(), heading)
            )

    # Sort headings according to their actual position in the resume
    heading_positions.sort(key=lambda x: x[0])

    # Extract the content between consecutive headings
    for i, (start, end, heading) in enumerate(heading_positions):

        # If this is not the last heading,
        # the next heading marks the end of this section
        if i + 1 < len(heading_positions):

            next_start = heading_positions[i + 1][0]

        # If this is the last heading,
        # extract everything until the end of the resume
        else:

            next_start = len(text)

        # Extract section content
        content = text[end:next_start].strip()

        # Store the section using lowercase heading as the key
        sections[heading.lower()] = content

    return sections