# Define a class Time
class Time:
    # Define maximum values for hours, minutes and seconds
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    # Constructor to initialize the object with hours, minutes and seconds
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Method to set new time
    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    # Method to get time in string format
    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    # Method to get the next second
    def next_second(self) -> str:
        # Increment seconds by 1
        self.seconds += 1
        # If seconds exceed maximum seconds, reset seconds to 0 and increment minutes by 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            # If minutes exceed maximum minutes, reset minutes to 0 and increment hours by 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                # If hours exceed maximum hours, reset hours to 0
                if self.hours > Time.max_hours:
                    self.hours = 0
        # Return the time in string format
        return Time.get_time(self)


# Test example
# Create a Time object with initial time 9:30:59
time = Time(9, 30, 59)
# Print the next second
print(time.next_second())
