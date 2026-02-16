**Local AI Assistant (Jarvis & Alfred)**

  This is a privacy-focused, cross-platform AI agent that was built to demonstrate Secure System Automation and Local LLM Integration. This project featured two specialized assistants: Jarvis (optimized for Mac) and Alfred (optimized for Windows)
  The point of this project was to explore AI and Cybersecurity out of curiosity. I am new to Python and wanted to not only test my skills but also learn along the way and see how AI works with Python.

  
**Overview**

  This project uses the Ollama framework and Llama 3 to keep it local. It provides the concept of an Assistant like Jarvis from Iron Man and Alfred from Batman that can control system applications while protecting sensitive data.


**Key Features**
•	Privacy First: All data happens on the device, no external servers
•	System Automation: Natural language control for opening applications such as browsers, notes, and music
•	Integrated IAM Layer: Custom Identity and Access Management (IAM) that intercepts restricted commands and requires a password to access
•	Contextual Memory: Implemented a conversation history that allows the AI to maintain and remember previous interactions

**Tech**

•	Language: Python
•	AI Engine: Ollama (Llama 3 Model) 
•	Libraries: os (System integration)

**Project Structure:**


•	Jarvis.py = MacOs version

•	Alfred.py = Windows version

•	Requirements.txt = Requirements for the project

•	README.md = Documentation of the project

**Prerequisites: **

•	Install Ollama and download the Llama 3 Model

•	In your terminal or cmd type: ollama pull llama3

**Security Implementations: **

1.	Least Privilege Enforcement: Users must provide a pre-defined admin_password to access restricted system applications (example: notepad)

2.	Error Handling: The try/except blocks help prevent the application from crashing during connection failures

  
