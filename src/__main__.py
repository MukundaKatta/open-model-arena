"""CLI for open-model-arena."""
import sys, json, argparse
from .core import OpenModelArena

def main():
    parser = argparse.ArgumentParser(description="Open-source LLM evaluation arena with crowd-sourced human preferences")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = OpenModelArena()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"open-model-arena v0.1.0 — Open-source LLM evaluation arena with crowd-sourced human preferences")

if __name__ == "__main__":
    main()
