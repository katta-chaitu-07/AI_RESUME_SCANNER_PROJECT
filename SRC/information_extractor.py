import re


# Skills that our resume scanner can currently detect
SKILLS = [
    "Python",
    "C++",
    "C",
    "Java",
    "SQL",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Natural Language Processing",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Git",
    "GitHub",
    "Streamlit",
    "Jupyter Notebook",
    "Google Colab",
    "VS Code",
    "Docker",
    "AWS",
    "Azure",
    "LLM",
    "LLMs",
    "Large Language Models",
    "Generative AI",
    "RAG",
    "LangChain",
    "Data Structures & Algorithms",
    "Object-Oriented Programming",
    "Regression",
    "Classification",
    "Model Evaluation",
    "TF-IDF",
    "Text Preprocessing",
    "Data Analysis",
    "Data Preprocessing",
    "Feature Engineering"
]


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


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):

            found_skills.append(skill)

    return found_skills


def extract_information(text):

    information = {}

    information["name"] = extract_name(text)
    information["email"] = extract_email(text)
    information["phone"] = extract_phone(text)
    information["skills"] = extract_skills(text)

    return information