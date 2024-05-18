# Visual Studio Project Creator (VSPC)

Visual Studio Project Creator (VSPC) is a Python script designed to streamline the setup and initialization of new project directories for Visual Studio Code. This tool simplifies the process of creating project folders and main files, making it easier to kickstart your development work.

## Features
- **Automated Setup**: Quickly create project directories and main files with user-defined names.
- **User-Friendly Interface**: Simple and intuitive prompts guide you through the setup process.
- **Integration with VSCode**: Automatically open your new project in Visual Studio Code.
- **Error Handling**: Provides clear error messages to ensure a smooth user experience.

## Installation
To get started with Visual Studio Project Creator (VSPC), follow these steps:

### Clone the Repository
1. Open a terminal or command prompt on your computer.
2. Navigate to the directory where you want to clone the repository. You can use the `cd` command to change directories. For example: `cd path/to/desired/directory`
3. Once you're in the desired directory, use the `git clone` command followed by the repository URL:
    ```sh
    git clone https://github.com/ImMirage/VSPC.git
    ```
4. After running the command, the repository will be cloned to your local machine.
5. You can now navigate to the cloned repository directory and start using VSPC.

### Usage
1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
2. Navigate to the VSPC directory using the terminal or command prompt.
3. Run the script using Python:
    ```sh
    python vspc.py
    ```
4. Follow the prompts to set up your project directory and main file.

## Compilation (Optional)
For seamless access and enhanced convenience, you can compile Visual Studio Project Creator (VSPC) using the Python module named `pyinstaller`. Follow these steps to compile VSPC into a standalone executable:

1. Install `pyinstaller` if you haven't already. You can do this using `pip`, the Python package installer, by running the following command:
    ```sh
    pip install pyinstaller
    ```
2. Once `pyinstaller` is installed, navigate to the directory where VSPC is located using the terminal or command prompt.
3. Run the following command to compile VSPC into a single executable file:
    ```sh
    pyinstaller --onefile vspc.py
    ```
4. After the compilation process is complete, navigate to the `dist` directory within the VSPC repository.
5. Locate the compiled executable file (it should be named `vspc.exe` if you're on Windows).
6. Move the executable file to a directory of your choice, preferably where you want to store your projects, for easy access.
7. You can now pin the compiled VSPC executable to your taskbar for quick and effortless usage.

## Compatibility
VSPC is compatible with Windows operating systems.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve VSPC.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
