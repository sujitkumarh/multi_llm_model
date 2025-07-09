from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import json

def run():
    config = json.load(open("config/ollama_config.json"))

    planner = AssistantAgent(name="planner", llm_config=config)
    coder = AssistantAgent(name="coder", llm_config=config)
    reviewer = AssistantAgent(name="reviewer", llm_config=config)
    user = UserProxyAgent(name="user", human_input_mode="NEVER", code_execution_config={"use_docker": False} )


    groupchat = GroupChat(agents=[user, planner, coder, reviewer], messages=[], max_round=5)
    manager = GroupChatManager(groupchat=groupchat, llm_config=config)
    user.initiate_chat(manager, message="Create a CLI script to backup a folder to a ZIP file.")
