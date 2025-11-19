# Kanban-Task-Tracker-CLI app
- Simple CLI tool to track tasks and manage your to-do list.

## Requirements:
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
- Add, Update, and Delete tasks

- Mark a task as in progress or done

- List all tasks

- List all tasks that are done

- List all tasks that are not done

- List all tasks that are in progress

#### constraints to guide the implementation:
- Use positional arguments in command line to accept user inputs.
- Use a JSON file to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the native file system module of your programming language to interact with the JSON file.
- No use of any external libraries or frameworks to build this project.
- Ensure to handle errors and edge cases gracefully.
  
## Features:









## Example
```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
# Output: Task deleted successfully (1. "Buy groceries and cook dinner")

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

```
