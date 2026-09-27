import re
import subprocess


def generate_answer(prompt):

    result = subprocess.run(
        ["ollama", "run", "llama3.2", prompt],
        capture_output=True,
        text=True
    )

    answer = result.stdout

    # Remove terminal cursor-control / ANSI escape sequences
    answer = re.sub(
        r'\x1b\[[0-9;?]*[ -/]*[@-~]',
        '',
        answer
    )

    # Remove leftover fragments from terminal cursor movements
    answer = re.sub(r'\d+DK', '', answer)
    answer = re.sub(r'\bK\b', '', answer)

    # Remove carriage returns
    answer = answer.replace('\r', '')

    # Clean up extra spaces
    answer = re.sub(r' +', ' ', answer)

    return answer.strip()