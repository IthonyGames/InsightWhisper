import pytesseract
from PIL import Image
import pyautogui
import pyperclip
import tkinter as tk
import openai
import os
import textwrap
import configparser
import keyboard


config_file = "config.ini"

if os.path.exists(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config.get("OpenAI", "api_key")
    openai.api_key = api_key

else:
    config = configparser.ConfigParser()
    config.add_section("OpenAI")
    api_key = ""


context_status = 0
context_status_label = ["Context ON", "Context OFF"]
context_status_color = ["#28a745", "#dc3545"]

context_type = 0
context_type_button_label = ["Copied text", "Screen"]

output_type = 2
output_type_button_label = ["Output", "Clipboard", "Paste"]

length_type = 3
length_button_label = ["Short", "Medium", "Long", "Length off"]
length_responses = [
    "Can you please provide me with a detailed response that is Short in length, smallest count of word?",
    "Can you provide me with a message that is Medium in length, that is around 2 Sentence in length?",
    "Could you please provide me with a message that is Long in length, that is approximately 2-3 paragraphs long?",
    "",
]
token_counts = [800, 1500, 2100, 1000]
token = token_counts[length_type]

root_ui = tk.Tk()

output_count = 0

role = "You are a helpful assistant."

temperature = 0.7

root_ui.configure(bg='#333')



def change_context_status():
    global context_status
    if context_status != (len(context_status_label)-1):
        context_status += 1
    else: 
        context_status = 0
    context_status_button.config(text=context_status_label[context_status], bg=context_status_color[context_status])
    context_type_button.config(bg=context_status_color[context_status])

def change_context_type():
    global context_type
    if context_type != (len(context_type_button_label)-1):
        context_type += 1
    else: 
        context_type = 0
    context_type_button.config(text=context_type_button_label[context_type])

def change_output_type():
    global output_type
    if output_type != (len(output_type_button_label)-1):
        output_type += 1
    else: 
        output_type = 0
    output_type_button.config(text=output_type_button_label[output_type], bg='#545454')

def change_length_type():
    global length_type
    if length_type != (len(length_button_label)-1):
        length_type += 1
    else: 
        length_type = 0
    length_type_button.config(text=length_button_label[length_type])

def response(prompt_text):
    global output_count, role
    print(prompt_text)
    output_count += 1
    if role_input.get() != "":
        role = role_input.get()
    else:
        role = "You are a helpful assistant."
    message = None
    message = [
        {"role": "system", "content": role}
    ]
    message.append({"role": "user", "content": prompt_text})
    response = send_api_request(message)
    if output_type == 0:
        wrapped_output = textwrap.fill(response, width=70)
        result.config(text=f"Output ({str(output_count)}): {wrapped_output}")
    elif output_type == 1:
        pyperclip.copy(response)
        result.config(text=f"Output ({str(output_count)})")
    elif output_type == 2:
        pyautogui.typewrite(response)
        result.config(text=f"Output ({str(output_count)})")

def send_api_request(request):
    global temperature, token
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=request,
        max_tokens=token,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].message.content

def process():
    global context_status, prompt
    if context_status == 0:
        if context_type == 0:
            context_text = str(pyperclip.paste())
            response(f"{prompt_input.get()} {length_responses[length_type]} \"{context_text}\"")
        else:
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            with Image.open('screenshot.png') as img:
                context_text = pytesseract.image_to_string(img)
            response(f"{prompt_input.get()} {length_responses[length_type]} \"{context_text}\"")
    else:
        response(f"{prompt_input.get()} {length_responses[length_type]}")

def call_response():
    prompt_text = str(pyperclip.paste())
    response(prompt_text)

# Define the key combination handler
def handle_key_combination():
    call_response()


context_status_button = tk.Button(root_ui, font=('Futura', 8), text=context_status_label[context_status], command=change_context_status)
context_status_button.config(text=context_status_label[context_status], bg=context_status_color[context_status])
context_status_button.pack(pady=2)

context_type_button = tk.Button(root_ui, font=('Futura', 8), text=context_type_button_label[context_type], command=change_context_type)
context_type_button.config(text=context_type_button_label[context_type], bg=context_status_color[context_status])
context_type_button.pack(pady=2)

output_type_button = tk.Button(root_ui, font=('Futura', 8), text=output_type_button_label[output_type], command=change_output_type)
output_type_button.config(text=output_type_button_label[output_type], bg='#545454')
output_type_button.pack(pady=2)

length_type_button = tk.Button(root_ui, font=('Futura', 8), text=length_button_label[length_type], command=change_length_type)
length_type_button.config(text=length_button_label[length_type], bg='#545454')
length_type_button.pack(pady=2)

prompt_label = tk.Label(root_ui, font=('Futura', 8), text="Enter Prompt:", bg='#333', fg='#fff')
prompt_label.pack()

prompt_input = tk.Entry(root_ui, width=30, bg='#545454')
prompt_input.pack(pady=2)

role_label = tk.Label(root_ui, font=('Futura', 8), text="Role:", bg='#333', fg='#fff')
role_label.pack()

role_input = tk.Entry(root_ui, width=30, bg='#545454')
role_input.pack(pady=2)

creativity_label = tk.Label(root_ui, font=('Futura', 8), text="Creativity:", bg='#333', fg='#fff')
creativity_label.pack()
creativity_slider = tk.Scale(root_ui, from_=0, to=10, orient=tk.HORIZONTAL, bg='#545454')
creativity_slider.pack(pady=2)



def update_label(val):
    global temperature
    temperature = float(val) / 10

creativity_slider.config(command=update_label)

def main():
    root_ui.title("InsightWhisper")
    root_ui.geometry("195x320")
    root_ui.attributes("-topmost", True) 
    process_button = tk.Button(root_ui, text="Generate Response", font=('Futura', 8), command=process, bg='#999')
    process_button.pack(pady=2)
    root_ui.mainloop()
    
result = tk.Label(root_ui, text="", bg='#333', fg='#fff')
result.pack()

if not os.path.exists(config_file):
    # Create a new configuration file
    config = configparser.ConfigParser()
    config.add_section("OpenAI")
    api_key = ""

    # Create the main Tkinter window
    root = tk.Tk()

    # Set the window attributes
    root.attributes("-topmost", True)
    root.title("OpenAI API Key")

    # Create a label for the API key input
    label = tk.Label(root, text="Enter your OpenAI API key:")
    label.pack()

    # Create an entry widget for the API key
    entry = tk.Entry(root)
    entry.pack()

    # Create a function to handle the button click
    def submit_key():
        # Retrieve the API key from the entry widget
        api_key = entry.get()

        # Save the API key to the configuration file
        config.set("OpenAI", "api_key", api_key)
        with open(config_file, "w") as file:
            config.write(file)

        # Set the OpenAI API key
        openai.api_key = api_key

        # Destroy the window
        root.destroy()

    # Create a button to submit the API key
    button = tk.Button(root, text="Submit", command=submit_key)
    button.pack()

    # Calculate the window position for centering
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Run the Tkinter event loop


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+alt+o', handle_key_combination)
    main()

