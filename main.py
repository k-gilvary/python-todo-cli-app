user_tasks = []

def main():
    run_program = True
    print('Welcome to the To Do List App! Select an action to get started (type 1, 2, 3, or 4):')

    while run_program:
        print('\n1. Add a task\n2. View tasks\n3. Delete a task\n4. Exit')
        user_action = input('\nEnter your choice: ')

        if user_action == '1':
            task_to_add = input('\nEnter the task you want to add: ')
            user_tasks.append(task_to_add)
            print(f'\nAdded task {task_to_add} successfully!')

        elif user_action == '2':
            if len(user_tasks) == 0:
                print('\nYou have no tasks yet! Try adding one!')
            else:
                print('\nYour tasks:\n')
                for i in range(len(user_tasks)):
                    print(f'{i+1}- {user_tasks[i]}\n\n')

        elif user_action == '3':
            task_to_delete = int(input('\nEnter the index of the task you want to delete (1, 2, 3, etc.): ')) - 1
            try: 
                deleted_task = user_tasks.pop(task_to_delete)
                print(f'\nDeleted task {deleted_task} successfully!')
            except IndexError:
                print('Invalid index. Please try again.')

        elif user_action == '4':
            print('\n\nGoodbye!\n\n')
            run_program = False
            
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()