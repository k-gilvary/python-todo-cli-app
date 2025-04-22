from modules.add_task import add_task
from modules.view_tasks import view_tasks
from modules.delete_task import delete_task

user_tasks = []

def main():
    run_program = True
    print('Welcome to the To Do List App! Select an action to get started (type 1, 2, 3, or 4):')

    while run_program:
        print('\n1. Add a task\n2. View tasks\n3. Delete a task\n4. Exit')
        user_action = input('\nEnter your choice: ')

        if user_action == '1':
            add_task(user_tasks)

        elif user_action == '2':
            view_tasks(user_tasks)

        elif user_action == '3':
            delete_task(user_tasks)

        elif user_action == '4':
            print('\n\nGoodbye!\n\n')
            run_program = False
            
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()