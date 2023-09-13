import time
from playsound import playsound

def set_alarm(alarm_time, alarm_message):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print(alarm_message)
            playsound('alarm_sound.mp3')  # Replace 'alarm_sound.mp3' with your desired alarm sound file
            break
        time.sleep(1)  # Check the time every second

if __name__ == "__main__":
    print("Welcome to the Alarm Clock App")
    alarm_time = input("Enter the alarm time (HH:MM:SS format): ")
    alarm_message = input("Enter the alarm message: ")
    
    set_alarm(alarm_time, alarm_message)
