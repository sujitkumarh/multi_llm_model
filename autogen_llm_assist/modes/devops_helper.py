from autogen import AssistantAgent, UserProxyAgent
from autogen.agentchat import GroupChat, GroupChatManager
import json

def run():
    config = json.load(open("config/ollama_config.json"))

    assistant = AssistantAgent(
        name="devops_bot",
        llm_config=config
    )

    def is_devops_related(prompt: str) -> bool:
        keywords = [
            "ansible", "docker", "kubernetes", "terraform",
            "ci/cd", "jenkins", "aws", "ubuntu", "linux",
            "restart", "apache", "nginx", "cloud", "server",
            "infrastructure", "prometheus", "grafana", "pipeline"
        ]
        return any(keyword in prompt.lower() for keyword in keywords)

    class StrictUserProxyAgent(UserProxyAgent):
        def get_human_input(self, prompt: str) -> str:
            message = input(prompt)
            if message.lower() in ["exit", "end"]:
                print("\n👋 Ending the conversation. Goodbye!\n")
                exit()

            if not is_devops_related(message):
                print("\n❌ This assistant only handles **DevOps-related** tasks. Please try again with a relevant query.\n")
                return self.get_human_input(prompt)

            return message

    user = StrictUserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={"use_docker": False}
    )

    class CustomGroupChatManager(GroupChatManager):
        def _process_received_message(self, sender, message, silent):
            if message.strip().lower() == "end":
                print("\n👋 Ending the conversation. Goodbye!\n")
                exit()
            super()._process_received_message(sender, message, silent)
            print("\n🔁 Would you like to continue the chat or type 'end' to exit?\n")

    groupchat = GroupChat(agents=[user, assistant], messages=[], max_round=5)
    manager = CustomGroupChatManager(groupchat=groupchat)

    initial_prompt = "Write an Ansible playbook to restart Apache server on 3 Ubuntu hosts."
    user.initiate_chat(assistant, message=initial_prompt)
