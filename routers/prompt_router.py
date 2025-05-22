import json
from models import MODEL_CLIENTS
from utils.context_injector import inject_context


async def route_prompt(data):
    user_prompt = data.get("prompt")
    model = data.get("model", "openai")
    use_task_planner = data.get("task_planner", False)

    with open("context/user_context.json") as f:
        context = json.load(f)

    client = MODEL_CLIENTS.get(model)
    if not client:
        return {"error": f"Model '{model}' not supported"}

    if use_task_planner:
        subtasks = split_into_subtasks(user_prompt)
        results = []
        for subtask in subtasks:
            full_prompt = inject_context(subtask, context)
            results.append(client.call(full_prompt))
        return {
            "subtasks": subtasks,
            "responses": results,
            "final": " ".join(results)
        }
    else:
        full_prompt = inject_context(user_prompt, context)
        return {"response": client.call(full_prompt)}