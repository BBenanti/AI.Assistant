import os
#imports the os module, which provides functions for interacting with the operating system
import ollama
#imports the ollama module, which is used for interacting with the Ollama API


admin_password = "123456789"  # Change this to a secure password

#Set Up AI Memory, starting with instructions for the AI to follow, which will help it understand how to respond to user inputs and what kind of behavior is expected from it.
convo_history = [
    {'role': 'system', 'content': 'You are Jarvis, a helpful and friendly AI assistant. You can perform tasks, answer questions, and assist with various activities. Always be polite and provide accurate information.'}
]

#This allows us to call back the code whenever we need to check the security of the program, without having to rewrite the code every time.
def check_security():
    #Ask the user for their password
    attempt = input("Enter the admin password to access Jarvis: ")

    #The Logic Gate (If/Else) to check if the password is correct
    if attempt == admin_password:
        print("Access granted!")
        return True #Tells the main program to continue
    else:
        print("Access denied! Incorrect password.")
        return False #Tells the main program to stop 
    

#Creating the actual chat bot function, which will be called if the user enters the correct password
def jarvis_chat():
    print("Welcome to Jarvis! How can I assist you today? Type 'exit' to end the chat.")

    #While loop to keep the chat going until the user decides to exit
    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase for easier comparison

        if user_input == "exit":
            print("Goodbye!")
            break


        elif "calculator" in user_input:
            print("Opening calculator...")
            os.system("open -a Calculator")  # This will open the calculator on the OS (-a is for macOS, windows users would use "calc.exe" or "calc")

            
        elif "notes" in user_input:
            print("Security Alert: This is a restricted app. Please enter the admin password to access it.")

            if check_security() == True:  # Calls the security check function
                print("Access granted! Opening Notes...")
                os.system("open -a Notes")  # This will open notepad on the OS   
            else:
                print("Access denied! Notes will not be opened.")
        
        elif "spotify" in user_input:
            print("Opening Spotify...")
            os.system("open -a Spotify")  # This will open Spotify on the OS
        
        elif "safari" in user_input:
            print("Opening Safari...")
            os.system("open -a Safari")  # This will open Safari on the OS
        else:
            # 2. ADD USER MESSAGE TO MEMORY
            convo_history.append({'role': 'user', 'content': user_input})

            try: #
                # 3. SEND THE WHOLE HISTORY TO AI
                response = ollama.chat(model='llama3', messages=convo_history)
                
                # Get the AI's answer
                ai_message = response['message']['content']
                
                print(f"Jarvis: {ai_message}")
                
                # Add the AI's answer to memory so it remembers it for next time
                convo_history.append({'role': 'assistant', 'content': ai_message})
                
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    jarvis_chat()

