"""A simplified Markdown editor"""
import os
import validators

def print_help():
    print("Available formatters: plain bold italic link inline-code header line-break ordered-list unordered-list")
    print("Special commands: !help !done")


def format_text(formatter, text):
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "header":
        return f"#{text}\n\n"
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        if validators.url(url):
            return f"[{label}]({url})"
        else:
            print("Invalid URL format.")
            return ""
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter in ["ordered-list", "unordered-list"]:
        try:
            num_items = int(input("Number of rows: "))
            if num_items > 0:
                formatted_text = ""
                for i in range(num_items):
                    item_text = input(f"Row #{i+1}: ")
                    formatted_text += f"{i+1}. " if formatter == "ordered-list" else "* "
                    formatted_text += f"{item_text}\n"
                return formatted_text
            else:
                print("The number of rows should be greater than zero")
                return ""
        except ValueError:
            print("Invalid input. Number of rows should be a number.")
            return ""
    elif formatter == "line-break":
        return "\n"
    else:
        print("Unknown formatting type or command")
        return ""


def save_to_file(text):
    if text:
        try:
            with open("output.md", "w") as file:
                file.write(text)
            print("Your markdown has been saved to 'output.md'.")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")
    else:
        print("Nothing to save.")


def markdown_formatter():
    formatted_text = ""
    while True:
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            save_to_file(formatted_text)
            break
        elif user_input in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "line-break"]:
            if user_input == "header" or user_input == "line-break":
                text = input("Text: ")
                formatted_text += format_text(user_input, text)
            else:
                text = input("Text: ")
                formatted_text += format_text(user_input, text)
            print("Your markdown:")
            print(formatted_text)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    markdown_formatter()

