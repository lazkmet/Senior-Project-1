///Qiskit///

This evaluation considered the Python library Qiskit. I used Anaconda to manage the environment, but virtual environment management is not required to use Qiskit.
The steps below use Visual Studio Code as the primary code editor for Qiskit.

Configuration Steps:

0. Make sure you have Python v. 3.7 or Later - If you do not have Python installed, you can install it here: https://www.python.org/downloads/

1. Create an empty environment (optional) - In your chosen environment manager, create an empty environment and set that as your current working directory.
Anaconda is a software tool that can be used for this, you can download it here: https://www.anaconda.com/products/distribution

2. Install Qiskit - Open a terminal, and run the command "pip install qiskit[visualization]" to install the necessary library components to run qiskit.
Note: If pip is not installed, you can find instructions to make sure it is installed here: https://pip.pypa.io/en/stable/installation/

3. Open your environment in your chosen code editor - Make sure you have the correct environment selected.
For VS Code, this requires using the Python: Select Interpreter command to choose the interpreter associated with your environment.
Use the shortcut Ctrl + Shift + P to open the full list of commands in VS Code.
Alternatively, you can open your code editor using a command prompt in Anaconda to automatically complete this association.
(open command prompt, run "code" to open VSCode)

4. Import the necessary elements for Qiskit - Use "from qiskit import [package]" as described in the documentation to access Qiskit functions.
This is explained in more detail in the tutorial listed here: https://qiskit.org/documentation/intro_tutorial1.html

For details on the functions available with Qiskit, you can read the documentation here: https://qiskit.org/documentation/index.html

