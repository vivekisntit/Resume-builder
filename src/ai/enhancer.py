from google import genai

MODEL_NAME = "gemini-2.5-flash"

def enhance_resume_data(input_data, client):

    guider_short = (
        "You are a resume assistant.\n"
        "Rewrite resume bullet points to be clear, precise and professional.\n"
        "Keep technical terms, metrics, and achievements intact.\n"
        "Return each bullet on a new line.\n"
        "Do not number them.\n"
        "Return only the improved bullet points."
    )

    guider_long = (
        "You are a resume assistant.\n"
        "Rewrite resume bullet points to be clear, precise and professional.\n"
        "If the input points are short, increase sentence length.\n"
        "If long enough, only fix grammar.\n"
        "Keep technical terms, metrics, and achievements intact.\n"
        "Return each bullet on a new line.\n"
        "Do not number them.\n"
        "Return only the improved bullet points."
    )

    def polish(text, prompt):
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"{prompt}\n\nPolish these resume bullet points:\n{text}"
        )
        return response.text.strip().split("\n")

    # Experience
    for exp in input_data.get("experience", []):
        if exp.get("description"):
            bullets = "\n".join(exp["description"])
            improved = polish(bullets, guider_long)
            exp["description"] = [b.strip("-• ") for b in improved if b.strip()]

    # Projects
    for proj in input_data.get("projects", []):
        if proj.get("description"):
            bullets = "\n".join(proj["description"])
            improved = polish(bullets, guider_long)
            proj["description"] = [b.strip("-• ") for b in improved if b.strip()]

    # Skills duties
    if input_data.get("skills", {}).get("duties"):
        bullets = "\n".join(input_data["skills"]["duties"])
        improved = polish(bullets, guider_short)
        input_data["skills"]["duties"] = [b.strip("-• ") for b in improved if b.strip()]

    return input_data