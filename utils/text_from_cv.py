def serialize_cv_for_translation(cv) -> str:
    skills = ', '.join(skill.name for skill in cv.skills.all())
    projects = ", ".join(p.name for p in cv.projects.all())
    contact = (
        f"Email: {cv.contacts.email}\n"
        f"Phone: {cv.contacts.phone}\n"
        f"LinkedIn: {cv.contacts.linkedin or 'N/A'}"
    )

    text = (
        f"Name: {cv.firstname} {cv.lastname}\n"
        f"Bio: {cv.bio}\n"
        f"Skills: {skills}\n"
        f"Projects:\n{projects}\n"
        f"Contact:\n{contact}"
    )
    return text
