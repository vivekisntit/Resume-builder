from openai import OpenAI

def enhance_resume_data(input_data, client):
    # prompt for project enhancement
    openai_guider_0=(
        "You are a resume assistant."
        "Rewrite resume bullet points to be clear, precise and professional."
        "Keep technical terms, metrics, and achievements intact."
        "Return only the improved bullet points."
    )
    # prompt for experience enhancement
    openai_guider_1=(
        "You are a resume assistant."
        "Rewrite resume bullet points to be clear, precise and professional."
        "If the input points are short, increase the sentence length."
        "If the input points are long enough already, don't change anything except for grammatical errors"
        "Keep technical terms, metrics, and achievements intact."
        "Return only the improved bullet points."
    )
    for exp in input_data.get("experience", []):
        if exp.get("description"):
            bullets = "\n".join(exp["description"])
            response = client.chat.completions.create(
                model= "gpt-4o-mini",
                messages=[
                    {"role": "system", "content": openai_guider_1},
                    {"role": "user", "content": f"Polish these resume bullet points:\n{bullets}"}
                ]
            )
            improved = response.choices[0].message.content.strip().split("\n")
            exp["description"] = [b.strip("-• ") for b in improved if b.strip()]
    for proj in input_data.get("projects", []):
        if proj.get("description"):
            bullets = "\n".join(proj["description"])
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": openai_guider_1},
                    {"role": "user", "content": f"Polish these resume bullet points:\n{bullets}"}
                ]
            )
            improved = response.choices[0].message.content.strip().split("\n")
            proj["description"] = [b.strip("-• ") for b in improved if b.strip()]
    # prompt for skills enhancement
    if input_data.get("skills", {}).get("duties"):
        bullets = "\n".join(input_data["skills"]["duties"])
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": openai_guider_0},
                {"role": "user", "content": f"Polish these resume bullet points:\n{bullets}"}
            ]
        )
        improved = response.choices[0].message.content.strip().split("\n")
        input_data["skills"]["duties"] = [b.strip("-• ") for b in improved if b.strip()]

    return input_data
