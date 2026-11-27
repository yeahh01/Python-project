# DOUBT TRACKER MANAGEMENT SYSTEM

doubts = []


# STUDENT SECTION

def student_section():

    while True:

        print("\n====== STUDENT SECTION ======")
        print("1. Add a Doubt")
        print("2. View My Doubts")
        print("3. Search My Doubt")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n------ ADD DOUBT ------")

            name = input("Enter your name: ")
            subject = input("Enter subject: ")
            question = input("Enter your doubt: ")

            doubt = {
                "name": name,
                "subject": subject,
                "question": question,
                "solution": "Not Provided",
                "status": "Pending"
            }

            doubts.append(doubt)

            print("\nYour doubt has been submitted!")

        elif choice == "2":

            name = input("\nEnter your name: ")

            found = False

            for i in range(len(doubts)):

                if doubts[i]["name"].lower() == name.lower():

                    print("\nDoubt Number:", i + 1)
                    print("Subject:", doubts[i]["subject"])
                    print("Question:", doubts[i]["question"])
                    print("Solution:", doubts[i]["solution"])
                    print("Status:", doubts[i]["status"])

                    found = True

            if found == False:
                print("No doubts found.")

        elif choice == "3":

            name = input("\nEnter your name: ")
            subject = input("Enter subject: ")

            found = False

            for doubt in doubts:

                if doubt["name"].lower() == name.lower() and doubt["subject"].lower() == subject.lower():

                    print("\nQuestion:", doubt["question"])
                    print("Solution:", doubt["solution"])
                    print("Status:", doubt["status"])

                    found = True

            if found == False:
                print("No doubt found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


# PROFESSOR SECTION

def professor_section():

    while True:

        print("\n====== PROFESSOR SECTION ======")
        print("1. View All Doubts")
        print("2. View Pending Doubts")
        print("3. Mark Doubt as Solved")
        print("4. Provide Solution")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n------ ALL STUDENT DOUBTS ------")

            if len(doubts) == 0:
                print("No doubts available.")

            else:

                for i in range(len(doubts)):

                    print("\nDoubt Number:", i + 1)
                    print("Student:", doubts[i]["name"])
                    print("Subject:", doubts[i]["subject"])
                    print("Question:", doubts[i]["question"])
                    print("Solution:", doubts[i]["solution"])
                    print("Status:", doubts[i]["status"])

        elif choice == "2":

            print("\n------ PENDING DOUBTS ------")

            found = False

            for i in range(len(doubts)):

                if doubts[i]["status"] == "Pending":

                    print("\nDoubt Number:", i + 1)
                    print("Student:", doubts[i]["name"])
                    print("Subject:", doubts[i]["subject"])
                    print("Question:", doubts[i]["question"])

                    found = True

            if found == False:
                print("No pending doubts.")

        elif choice == "3":

            if len(doubts) == 0:
                print("No doubts available.")

            else:

                for i in range(len(doubts)):

                    print("\nDoubt Number:", i + 1)
                    print("Student:", doubts[i]["name"])
                    print("Question:", doubts[i]["question"])
                    print("Status:", doubts[i]["status"])

                number = int(input("\nEnter doubt number to solve: "))

                if number >= 1 and number <= len(doubts):

                    doubts[number - 1]["status"] = "Solved"

                    print("\nDoubt marked as solved!")

                else:
                    print("Invalid doubt number.")

        elif choice == "4":

            print("\n------ PROVIDE SOLUTION ------")

            if len(doubts) == 0:
                print("No doubts available.")

            else:

                for i in range(len(doubts)):

                    print("\nDoubt Number:", i + 1)
                    print("Student:", doubts[i]["name"])
                    print("Subject:", doubts[i]["subject"])
                    print("Question:", doubts[i]["question"])

                number = int(input("\nEnter doubt number: "))

                if number >= 1 and number <= len(doubts):

                    solution = input("Enter solution: ")

                    doubts[number - 1]["solution"] = solution
                    doubts[number - 1]["status"] = "Solved"

                    print("\nSolution provided successfully!")

                else:
                    print("Invalid doubt number.")

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# MAIN PROGRAM

while True:

    print("\n================================")
    print("       DOUBT TRACKER")
    print("================================")

    print("1. Student")
    print("2. Professor")
    print("3. Exit")

    choice = input("\nAre you a Student or Professor? ")

    if choice == "1":

        student_section()

    elif choice == "2":

        professor_section()

    elif choice == "3":

        print("\nThank you for using Doubt Tracker!")
        break

    else:
        print("\nInvalid choice! Please try again.")