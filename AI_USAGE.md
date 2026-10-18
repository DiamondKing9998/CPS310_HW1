# AI Usage Report

## Tools Used
- ChatGPT (OpenAI)
- Claude Code (Anthropic)

## How AI Was Used
I primarily used ChatGPT to help plan the FRC-themed inventory manager, break down the assignment into smaller tasks, outline the required Python functions, and identify input validation and testing requirements.

I did also use ChatGPT to help structure the final README.md.

I also used Claude Code once to debug an issue relating to a str object not being able to be modified by individual characters.

## Example Prompts
Representative prompts included:
- "I want to design a frc inventory program (not super robust but a Proof of concept for the assignment)."
- "lets start with the simple menu, provide the general structure of the code but not the code itself."
- "why is add_item(inventory) erroring: TypeError: 'str' object does not support item assignment" (ai also had access to read the file contents)


## Suggestions Accepted
- Using FRC robot components as sample inventory data.
- Separating the program into functions for each inventory operation.
- Using a list of dictionaries and a pipe-separated text file.
- Building and committing program features incrementally.

## Suggestions Rejected or Modified
The initial design my AI considered Java classes and a graphical interface, as its personal intelligence automatically assumed I would want to write this in Java due to previous chats. After reviewing the assignment instructions, the design was instead simplified to a Python command-line application using lists, dictionaries, and text files.

## Verification
I ran into a few runtime errors throughout the process, with most of them being simple enough to fix with a little help from Google. The previously mentioned issue I used Claude Code for was the only issue I needed direct AI assistance with.

## Code Understanding
AI was able to help me greater understand some Python library functions that I otherwise probably wouldn't of used by suggesting them while breaking down the steps to finish this assignment. Enumerate was the big one.
