def inject_context(prompt: str, context: dict) -> str:
    injected = (
        f"User Context:\n"
        f"- Name: {context.get('name')}\n"
        f"- Writing Style: {context.get('writing_style')}\n"
        f"- Goals: {context.get('goals')}\n"
        f"- Preferred Tone: {context.get('tone')}\n\n"
        f"Instruction: Please generate a response that matches the above user context.\n\n"
        f"User Prompt: {prompt}"
    )
    return injected