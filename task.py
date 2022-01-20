import sys

# add
def addTask(priority, task):
    # try:
    #     task = open('task.txt')
    #     lines = task.readlines()
    #     if lines:
    #         if lines[0][0].isnumeric():
    #             for n, line in enumerate(lines):
    #                 if line[0] == priority:
    #                     line[0] += 
    #                     return f'Task with this priority al'
    #     file = open('task.txt', 'a')
    #     file.write(f'{priority} {task}\n')
    # except:
    file = open('task.txt', 'a')
    file.write(f'{priority} {task}\n')
    return f'Added task: "{task}" with priority {priority}'

# ls
def ls():
    try:
        tasks = open('task.txt', 'r')
    except:
        return "There are no pending tasks!"
    task = []
    for n, line in enumerate(tasks):
        if line[0].isnumeric():
            task.append((f'{n + 1}.{line[1:-1]} [{line[0]}]'))
    if task == []:
        return "There are no pending tasks!"
    return "\n".join(task)

# del
def deleteTask(index):
    file = open('task.txt', 'r')
    lines = file.readlines()
    if index > len(lines) or index < 1:
        return f'Error: task with index #{index} does not exist. Nothing deleted.'
    del lines[index - 1]
    file = open('task.txt', 'w')
    file.writelines(lines)
    return f'Deleted task #{index}'

# done
def done(index):
    file = open('completed.txt', 'a')
    task = open('task.txt', 'r')
    lines = task.readlines()
    if index > len(lines) or index < 1:
        return f'StringContaining "Error: no incomplete item with index #{index} exists.'
    file.write(lines[index - 1][2:])
    deleteTask(index)
    return "Marked item as done."

# help


def help():
    usage = '''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics'''
    return usage

# report
def report():
    completed = open('completed.txt', 'r')
    tasks = open('task.txt', 'r')
    task = []
    comp = []
    report = []
    for n, line in enumerate(tasks):
        task.append((f'{n + 1}.{line[1:-1]} [{line[0]}]\n'))
    for n, line in enumerate(completed):
        comp.append((f'{n + 1}. {line[:-1]}'))
    report.append((f'Pending : {len(task)}'))
    report += task
    report.append((f'Completed : {len(comp)}'))
    report += comp
    return "\n".join(report)


if __name__ == "__main__":
    try:
        cmd = sys.argv[1]
        noArgvLs = ["ls", "help", "report"]
        oneArgvLs = ["del", "done"]
        if cmd in noArgvLs:
            print(locals()[cmd]())
        elif cmd == 'add':
            if sys.argv[3:]:
                print(addTask(sys.argv[2], ' '.join(sys.argv[3:])))
            else:
                print("Error: Missing tasks string. Nothing added!")
        elif cmd in oneArgvLs:
            try:
                if cmd == 'del':
                    cmd = "deleteTask"
                print(print(locals()[cmd](int(sys.argv[2]))))
            except Exception as e:
                text = {"deleteTask": "deleting tasks",
                        "done": "marking tasks as done"}
                print(f'Error: Missing NUMBER for {text[cmd]}.')
                print(e)
        else:
            print(help())
    except:
        print(help())
