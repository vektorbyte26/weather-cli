# Generated with ChatGPT
import argparse
import json
from pathlib import Path


def format_weather(data):
    return f"{data['city']}: {data['temperature_c']} C, {data['condition']}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    print(format_weather(json.loads(Path(args.file).read_text(encoding="utf-8"))))
