# write function to moniter CPU uses and get alert
# use psutil library to get CPU information 
# use keyboard library to detect key press
import psutil
import keyboard 

CPU_USAGES_THRESHOLD_WARN_LIMIT = 80

def moniter_cpu_usages():
    try:
        print("==== Monitoring CPU usages. Press ESC key to stop ====")
        while True:
            if keyboard.is_pressed('esc'):
                print("CPU Monitoring Stop....")
                break

            cpu_usages = psutil.cpu_percent()
            print(f"CPU usages : {cpu_usages}%")

            if cpu_usages > CPU_USAGES_THRESHOLD_WARN_LIMIT:
                print(f"Alert! CPU usage exceeds threshold:  {cpu_usages}%")

    except Exception as e:
        print(f"Critical error : {e}")



# Call moniter_cpu_usages function
moniter_cpu_usages()