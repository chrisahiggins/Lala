---
name: add
description: Adds two numbers together and outputs the result. Use this skill whenever the user asks to add two numbers, e.g. "add 3 and 5", "/add 10 20", or "what is 7 plus 4".
---

# Add Two Numbers

When invoked, run the bundled Python script with the two numbers passed as arguments and report the result.

## Steps

1. Extract the two numbers from the user's input (they may be passed as arguments or stated in the prompt).
2. Run the script:
   ```
   python scripts/add.py <number1> <number2>
   ```
3. Output the result to the user.

## Example

User: `/add 12 30`

You run: `python scripts/add.py 12 30`

Script outputs: `42.0`

You respond: `42`
