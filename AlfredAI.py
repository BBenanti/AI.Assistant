import os #importing the operating system to open up applications
import ollama #importing ollama as my local AI agent 

admin_password = "12345" #This is the password that is used to enter sensitive applications

convo_history = [
    {"role": "system", "content": "You are Alfred, a helpful and friendly AI assistant. You can perform tasks, answer questions, and assist with various tasks. Always be polite and provide acurate information"}
]

def check_security():
    attempt= input("Enter the admin password: ") #Asks user for the password on restricted application

    if attempt == admin_password: 
        print("Access Granted!")
        return True #Tells program to continue 
    
    else:
        print("Access Denied")
        return False #Tells program to stop

#Main AI Program
def alfred_chat():
    print("Hello I am Alfred, how may I assist you today! To end the chat please type 'exit'")

#Creating a while loop to keep the chat going unless the user exits
    while True:
        user_input = input('You: ').lower()

        if user_input == "exit":
            print('Have a nice day!')
            break
    
        elif "brave" in user_input:
            print('Opening Brave Browser...')
            os.system('start brave')

        elif "spotify" in user_input:
            print('Opening Spotify...')
            os.system('start spotify')
        
        elif "notepad" in user_input:
            print('This requires an admin password. Please type it in to continue: ')

            if check_security() == True:
                print('Access Granted!')
                os.system('start notepad')
            else: 
                print('Access Denied')
        
        else:
            convo_history.append({'role': 'user', 'content': user_input})

            try:
                response = ollama.chat(model='llama3', messages=convo_history)

                ai_message = response['message']['content']

                print(f'Alfred: {ai_message}')

                convo_history.append({'role': 'assistant', 'content': ai_message})

            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    alfred_chat()
    









