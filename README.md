# InsightWhisper

## Description
InsightWhisper is a Python-based chatbot that utilizes OpenAI's GPT-3.5 model to provide interactive responses. It can generate responses based on user prompts and interact with the user through a graphical user interface (GUI).

The AI Assistant uses optical character recognition (OCR) to extract text from either the screen or the clipboard. It supports context-aware conversations and allows the user to toggle various settings such as context, input type, output display, and response length.

## Features
- Context-aware conversations: Toggle context on/off to provide the AI Assistant with conversation history.
- Input from screen or clipboard: Choose whether to input text from the screen or clipboard using OCR.
- Output display options: Choose to display the response in the GUI or copy it to the clipboard.
- Adjustable response length: Select short, medium, or long response lengths based on your needs.
- Role customization: Customize the role of the AI Assistant in the conversation.

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/ai-assistant.git`
2. Navigate to the project directory: `cd insightwhisper`
3. Install the required libraries: `pip install -r requirements.txt`
4. Install Tesseract OCR by following these steps:
   - Download Tesseract OCR from the official repository: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install Tesseract OCR on your system.
   - Add Tesseract OCR to the PATH environment variable. Here's how to do it:
     - On Windows:
       - Open the Control Panel and go to System.
       - Click on "Advanced system settings" and then click on the "Environment Variables" button.
       - In the "System variables" section, select the "Path" variable and click on the "Edit" button.
       - Add the path to the Tesseract OCR installation directory (e.g., `C:\Program Files\Tesseract-OCR`) to the list of paths.
       - Click "OK" to save the changes.
     - On macOS and Linux:
       - Open a terminal window.
       - Run the following command, replacing `/path/to/tesseract` with the actual path to the Tesseract OCR installation directory:
         ```
         export PATH=$PATH:/path/to/tesseract
         ```
5. Run the code: `python InsightWhisper.py`

## Usage
1. Launch the AI Assistant by running the `InsightWhisper.py` file.
2. Enter a prompt in the prompt input field.
3. Adjust the settings as desired:
   - Toggle context on/off using the "Context ON/OFF" button.
   - Choose input type (screen or clipboard) using the "Type context" button.
   - Choose output display (GUI or clipboard) using the "Output" button.
   - Adjust response length (short, medium, or long) using the "Medium" button.
   - Customize the role of the AI Assistant by entering it in the "Role" input field.
   - Adjust the creativity level using the slider.
4. Click the "Generate Response" button to generate a response based on the prompt and settings.
5. The response will be displayed in the GUI or copied to the clipboard, based on the chosen output display.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
