meetings = []

def schedule_meeting():
    title = input("Enter meeting title: ")
    date = input("Enter meeting date: ")
    time = input("Enter meeting time: ")
    meetings.append({"title": title, "date": date, "time": time})
    print("Meeting scheduled")

def view_meetings():
    if not meetings:
        print("No meetings scheduled")
    else:
        for meeting in meetings:
            print(meeting["title"], "-", meeting["date"], "-", meeting["time"])

def main():
    while True:
        print("1. Schedule Meeting")
        print("2. View Meetings")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            schedule_meeting()
        elif choice == "2":
            view_meetings()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
