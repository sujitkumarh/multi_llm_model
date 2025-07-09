import argparse
from modes import screenshot_bot, devops_helper, multi_agent_coder

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["screenshot", "devops", "coder"], required=True)
    args = parser.parse_args()

    if args.mode == "screenshot":
        screenshot_bot.run()
    elif args.mode == "devops":
        devops_helper.run()
    elif args.mode == "coder":
        multi_agent_coder.run()
