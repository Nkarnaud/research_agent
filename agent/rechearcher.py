from dotenv import load_dotenv
import aisuite as ai

load_dotenv()

# Initialize the AI Suite with your API key
CLIENT = ai.Client()


def  generate_draft_researche_paper(topic: str, model: str = "openai:gpt-4o") -> str:
    """
    Generate a draft researcher response based on the given prompt.
    Args:
        prompt (str): The research prompt or question.
        model (str): The AI model to use for generating the response.
    Returns:
        str: The generated research response.
    """
    prompt = f"""
    As a researcher specializing in {topic}, 
    please provide a comprehensive overview of the latest developments, key challenges,
    and future directions in this field. Include relevant studies, 
    statistics, and expert opinions to support your analysis.
    """
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )
    return response.choices[0].message["content"]


def reflect_on_draft(draft: str, model: str = "openai:o4-mini") -> str:
    """
    Reflect on the draft research paper and provide feedback for improvement.
    Args:
        draft (str): The draft research paper.
        model (str): The AI model to use for generating feedback.
    Returns:
        str: The feedback and suggestions for improvement.
    """
    prompt = f"""
    Please review the following draft research paper and provide constructive feedback. 
    address issuess structure, clarity, strength of argument, and writing style.
    and recommend any relevant studies or data that should be included.

    Draft:
    {draft}
    """
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )
    return response.choices[0].message["content"]


def revise_draft(draft: str, reflection: str, model: str = "openai:gpt-4o") -> str:
    """
    Revise the draft research paper based on the provided feedback.
    Args:
        draft (str): The original draft research paper.
        feedback (str): The feedback and suggestions for improvement.
        model (str): The AI model to use for revising the draft.
    Returns:
        str: The revised research paper.
    """
    prompt = f"""
    Please revise the following draft research paper based on the provided feedback. 
    Ensure that the revisions address all points raised in the feedback and enhance 
    the overall quality of the paper.

    Draft:
    {draft}

    reflection:
    {reflection}

    response:
    Response = {
        "revised_draft": "The revised research paper text.",
        "summary_of_changes": "A brief summary of the key changes made.",
        "additional_references": "Any new references or studies included."
    }

    """
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )
    return response.choices[0].message["content"]


if __name__ == "__main__":
    essay_prompt = "Should social media platforms be regulated by the government?"

    # Agent 1 – Draft
    draft = generate_draft(essay_prompt)
    print("📝 Draft:\n")
    print(draft)

    # Agent 2 – Reflection
    feedback = reflect_on_draft(draft)
    print("\n🧠 Feedback:\n")
    print(feedback)

    # Agent 3 – Revision
    revised = revise_draft(draft, feedback)
    print("\n✍️ Revised:\n")
    print(revised)
