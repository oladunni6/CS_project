room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

def get_course_details(course_number):
    room = room_numbers.get(course_number)
    instructor = instructors.get(course_number)
    meeting_time = meeting_times.get(course_number)

    if room and instructor and meeting_time:
        return (room, instructor, meeting_time)
    else:
        return None

def main():
    course_number = input("Enter a course number : ")
    course_details = get_course_details(course_number)

    if course_details:
        room, instructor, meeting_time = course_details
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Course number not found. Try Again.")

if __name__ == "__main__":
    main()