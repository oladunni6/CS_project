def calculate_alarm_time():
    # Ask the user for the current time in hours (24-hour format)
    current_time = int(input("Enter the current time (in hours, 0-23): "))
    
    # Validate the current time input
    if current_time < 0 or current_time > 23:
        print("Invalid time. Please enter a value between 0 and 23.")
        return
    
    # Ask the user for the number of hours to wait for the alarm
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
    
    # Calculate the alarm time
    alarm_time = (current_time + hours_to_wait) % 24
    
    # Display the alarm time
    print(f"The alarm will go off at {alarm_time:02d}:00.")

# Run the function
calculate_alarm_time()
