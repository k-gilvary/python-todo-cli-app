def delete_task(tasks):
    try: 
        task_to_delete = int(input('\nEnter the index of the task you want to delete (1, 2, 3, etc.): ')) - 1
        deleted_task = tasks.pop(task_to_delete)
        print(f'\nDeleted task {deleted_task} successfully!')
    except IndexError:
        print('Invalid index. Please try again.')
    except ValueError:
        print('Invalid input. Please enter a number.')

export = {
    'delete_task': delete_task
}