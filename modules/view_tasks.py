def view_tasks(tasks):
    if len(tasks) == 0:
        print('\nYou have no tasks yet! Try adding one!')
    else:
        print('\nYour tasks:\n')
        for i in range(len(tasks)):
            print(f'{i+1}- {tasks[i]}\n\n')

export = {
    'view_tasks': view_tasks
}