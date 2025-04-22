def add_task(tasks):
    task_to_add = input('\nEnter the task you want to add: ')
    if task_to_add.strip() == '':
        print('You cannot add an empty task. Please try again.')
    else:
        tasks.append(task_to_add)
        print(f'\nTask "{task_to_add}" added successfully!')
    
    return tasks

export = {
    'add_task': add_task
}