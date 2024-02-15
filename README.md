# JarvisVRApp

JarvisVRApp is a virtual assistant application developed in Python using PyQt5 for the graphical user interface. It provides various features such as date and time display, weather information, email sending, music playback, and more, all accessible through an intuitive user interface.

## Prerequisites
Before you begin working with JarvisVRApp, ensure you have the following prerequisites installed:

- **Python 3.8 or later**: Download and install Python from the [official website](https://www.python.org/downloads/).
- **Docker**: Install Docker from the [official Docker website](https://www.docker.com/get-started) to manage containerization.
- **Git**: Install Git from the [official Git website](https://git-scm.com/downloads) for version control and cloning the project repository.
- **Code Editor**: Choose a code editor or integrated development environment (IDE) of your preference. Popular choices include Visual Studio Code, PyCharm, or Atom.

## Project Structure
<pre>
JarvisVRApp/
├── Features/
│   ├── feature1.py
│   ├── feature2.py
│   └── ...
├── main.py
├── Dockerfile
└── requirements.txt
</pre>

## Jarvis Features 
Here's an overview of how Jarvis utilizes Python to execute each feature:

1. **Date & Time Display**:
   - Jarvis uses Python's `datetime` module to get the current date and time.
   - The retrieved date and time are displayed in the application's user interface using PyQt5.

2. **Weather Information**:
   - Jarvis fetches weather information from an online weather API using the `requests` library in Python.
   - The received weather data is then parsed and displayed in the application's user interface.

3. **Email Sending**:
   - Jarvis uses the `smtplib` library in Python to send emails.
   - The application prompts the user to input the necessary email details such as recipient, subject, and body.
   - After gathering the required information, Jarvis composes an email message and sends it using the SMTP protocol.

4. **Music Playback**:
   - Jarvis leverages the `pygame` library in Python for playing music files.
   - The application allows the user to select and play music files stored on the local system.

5. **Google Search**:
   - Jarvis utilizes Python's `webbrowser` module to perform Google searches.
   - The application prompts the user to input the search query, and then Jarvis opens the default web browser with the search results.

6. **Process Management**:
   - Jarvis utilizes the `psutil` library in Python to retrieve information about running processes.
   - The application gathers process data such as PID, name, memory usage, etc., and displays it in the user interface.

7. **Calculator**:
   - Jarvis uses Python to perform basic arithmetic calculations.
   - The application provides a graphical user interface with buttons for numbers, operators, and functions to allow the user to input calculations.

8. **Calendar**:
   - Jarvis employs PyQt5's `QCalendarWidget` to provide a calendar interface.
   - The application allows the user to view and interact with a calendar, including adding, editing, and deleting events.

9. **WhatsApp Integration**:
   - Jarvis integrates with the WhatsApp API using the `pywhatkit` library in Python.
   - The application prompts the user to input the recipient's phone number, message content, and optional parameters such as time delay for scheduling messages.

10. **Recipes Exploration**:
   - JarvisVRApp provides users with access to a curated collection of recipes.
   - Users can explore these recipes directly within the application, including details such as ingredients


## Installation
1. **Clone the repository:**
```bash
git clone https://github.com/FilcuAlexandru/JarvisVRApp-Python.git
```

2. **Navigate to the project directory:**
```bash
cd JarvisVRApp
```

3. **Build the Docker image:**
```bash
docker build -t jarvis-app .
```

4. **Run the Docker container:**
```bash
docker run -it --rm jarvis-app
```

## For Windows Use 

To be performed outside the container!

Creating a Windows Executable for JarvisVRApp

To distribute JarvisVRApp as a standalone executable for Windows users, you can use PyInstaller, a popular Python packaging tool. PyInstaller bundles your Python application and its dependencies into a single executable file, making it easy to run on Windows systems without needing to install Python separately.

## Prerequisites

Before you begin, make sure you have the following:

- **Python**: Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **PyInstaller**: Install PyInstaller using pip, the Python package manager:

    ```bash
    pip install pyinstaller
    ```

- **JarvisVRApp Source Code**: Make sure you have the source code for JarvisVRApp, including the `main.py` file and any other necessary files.

## Steps

1. **Navigate to Project Directory**: Open a command prompt or terminal window and navigate to the directory where your `main.py` file is located.

2. **Generate the Executable**: Run PyInstaller with the appropriate options to create the executable. Use the following command:

    ```bash
    pyinstaller --onefile main.py
    ```

    This command generates a single executable file (`main.exe`) in the `dist` directory of your project.

3. **Optional: Customize the Executable**: PyInstaller provides options to customize the generated executable, such as specifying an icon or including additional files. You can explore these options in the [PyInstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).

4. **Test the Executable**: Once the executable is generated, test it by running `main.exe` on a Windows machine. Ensure that it behaves as expected and includes all the functionality of your JarvisVRApp.

5. **Distribute the Executable**: Once you're satisfied with the executable, you can distribute it to others for use on Windows machines. You may want to include instructions or a README file to guide users on how to run the executable and any prerequisites they need to install.

## Notes

- PyInstaller bundles the Python interpreter and all necessary dependencies into the executable, eliminating the need for users to have Python installed.
- Depending on the complexity of your application and its dependencies, the size of the generated executable may vary.
- It's recommended to test the executable on different versions of Windows to ensure compatibility.
- Keep your `main.py` and other source files well-documented and organized for easier maintenance and troubleshooting.

By following these steps, you can create a Windows executable for JarvisVRApp and make it more accessible to users who may not have Python installed on their systems.
