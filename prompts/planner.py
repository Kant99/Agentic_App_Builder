def planner_prompt (user_prompt:str) -> str:
     PLANNER_PROMPT=f"""
    You are the planner, convert the user's prompt into a complete development plan.
    The user's prompt is: {user_prompt}
    """
     return PLANNER_PROMPT