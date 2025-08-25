import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a pokedex app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if args.verbose:
        print("User prompt:", args.user_prompt)

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
    ]

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print(f"Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print(f"Response:\n{response.text}")

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
    main()
