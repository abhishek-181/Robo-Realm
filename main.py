import subprocess

if __name__ == '__main__':

    print("Welcome to the RoboRealm 1.0 on Windows, Created by Abhishek.")
    print("To end this program please enter q.\n")

    powershell_command = fr'''
    Add-Type -AssemblyName System.Speech
    $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speechSynthesizer.Speak("Welcome to the RoboRealm 1.0 on Windows , Created by Abhishek.")
    '''
    subprocess.run(["powershell", "-Command", powershell_command])

    while True:

        # Take user-1 input
        user_1_input = input("User-1: ")

        if user_1_input == 'q':
            print(
                "Good Bye! -- RoboRealm is shutting down now. Please initiate the program again if you want to enter into RoboRealm.")

            powershell_command = fr'''
            Add-Type -AssemblyName System.Speech
            $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
            $speechSynthesizer.Speak("Good Bye! -- RoboRealm is shutting down now. Please initiate the program again if you want to enter into RoboRealm.")
            '''
            subprocess.run(["powershell", "-Command", powershell_command])

            break

        # converting user-1 input as speech using Powershell command --Speak function
        powershell_command = fr'''
        Add-Type -AssemblyName System.Speech
        $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
        $speechSynthesizer.Speak("{user_1_input}")
        '''

        # executing Powershell command for user-1
        subprocess.run(["powershell", "-Command", powershell_command])

        # Take user-2 input
        user_2_input = input("User-2: ")

        if user_2_input == 'q':
            print(
                "Good Bye! -- RoboRealm is shutting down now. Please initiate the program again if you want to enter into RoboRealm.")

            powershell_command = fr'''
            Add-Type -AssemblyName System.Speech
            $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
            $speechSynthesizer.Speak("Good Bye! -- RoboRealm is shutting down now. Please initiate the program again if you want to enter into RoboRealm.")
            '''
            subprocess.run(["powershell", "-Command", powershell_command])

            break

        # converting user-2 input as speech using Powershell command --Speak function
        powershell_command = fr'''
        Add-Type -AssemblyName System.Speech
        $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
        $speechSynthesizer.Speak("{user_2_input}")
        '''

        # executing Powershell command for user-2
        subprocess.run(["powershell", "-Command", powershell_command])










