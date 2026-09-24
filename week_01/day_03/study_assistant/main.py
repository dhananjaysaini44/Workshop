from learning_service import learn_topic
from flashcard_service import flashcard_topic
from interview_service import interview_topic
from quiz_service import quiz_topic

def menu():
    print("\n=== AI Study Assistant ===")
    print("1. Learning Module")
    print("2. Flashcards")
    print("3. Interview")
    print("4. Quiz")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter topic: ")
            print(learn_topic(topic))

        elif choice == "2":
            topic = input("Enter topic: ")
            print(flashcard_topic(topic))

        elif choice == "3":
            topic = input("Enter topic: ")
            print(interview_topic(topic))

        elif choice == "4":
            topic = input("Enter topic: ")
            print(quiz_topic(topic))

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()