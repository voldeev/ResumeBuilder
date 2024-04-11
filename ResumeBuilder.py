from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class ResumeBuilder:
    def __init__(self):
        self.resume = {}

    def add_position(self):
        position = input("Enter your desired position: ")
        self.resume['Position'] = position

    def add_contact_info(self):
        name = input("Enter your full name: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        city = input("Enter your city: ")
        self.resume['Name'] = name
        self.resume['Contacts'] = {"Phone": phone, "Email": email}
        self.resume['City'] = city

    def add_summary(self):
        summary = input("Enter a summary of your experience: ")
        self.resume['Summary'] = summary

    def add_technical_skills(self):
        tech_stack = {}
        print("Enter your technical skills (press Enter to stop):")
        while True:
            skill = input("Skill: ")
            if not skill:
                break
            proficiency = input("Proficiency level: ")
            tech_stack[skill] = proficiency
        self.resume['Technical Skills'] = tech_stack

    def add_experience(self):
        experience_list = []
        print("Enter your work experience (press Enter for next section):")
        while True:
            experience = {}
            company = input("Enter company name: ")
            if not company:
                break
            role = input("Enter your role: ")
            duration = input("Enter duration (e.g., 2019 - Present): ")
            description = input("Enter description: ")
            experience['Company'] = company
            experience['Role'] = role
            experience['Duration'] = duration
            experience['Description'] = description
            experience_list.append(experience)
        self.resume['Experience'] = experience_list

    def add_education(self):
        education = input("Enter your education: ")
        self.resume['Education'] = education

    def add_language_proficiency(self):
        languages = {}
        print("Enter your language proficiency (press Enter to stop):")
        while True:
            language = input("Language: ")
            if not language:
                break
            proficiency = input("Proficiency level: ")
            languages[language] = proficiency
        self.resume['Language Proficiency'] = languages

    def add_additional_info(self):
        additional_info = input("Enter any additional information: ")
        self.resume['Additional Info'] = additional_info

    def generate_resume(self):
        return self.resume

# Example Usage:
builder = ResumeBuilder()
builder.add_position()
builder.add_contact_info()
builder.add_summary()
builder.add_technical_skills()
builder.add_experience()
builder.add_education()
builder.add_language_proficiency()
builder.add_additional_info()
resume = builder.generate_resume()

# Create PDF Resume
doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
styles = getSampleStyleSheet()

content = []

# Convert resume information to HTML for display in PDF
for section, content_item in resume.items():
    content.append(Paragraph(f"<strong>{section}</strong>", styles["Heading1"]))
    if isinstance(content_item, dict):
        for key, value in content_item.items():
            content.append(Paragraph(f"<strong>{key}:</strong> {value}", styles["Normal"]))
    elif isinstance(content_item, list):
        for item in content_item:
            for key, value in item.items():
                content.append(Paragraph(f"<strong>{key}:</strong> {value}", styles["Normal"]))
            content.append(Spacer(1, 12))  # Spacer between blocks
    else:
        content.append(Paragraph(f"<strong>{content_item}</strong>", styles["Normal"]))
    content.append(Spacer(1, 12))  # Spacer between blocks

doc.build(content)
