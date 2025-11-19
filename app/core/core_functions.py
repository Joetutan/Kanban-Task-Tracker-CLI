from datetime import datetime
import json
from pathlib import Path

file = Path("./app/core/data.json")

if file.exists():
    with open(file, "r") as f:
        tasks = json.load(f)
else:
    tasks = {}

time_stamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

def add_task(description: str) -> None:
    
    task_id = len(tasks)+1
    while str(task_id) in tasks:
                task_id += 1
    tasks[task_id] = {
                        "description": description,
                        "task_id": task_id,
                        "status": "to-do",
                        "createAt": time_stamp,
                        "updatedAt": None
    }
    with open(file, "w") as f:
                json.dump(tasks, f, indent=4)
    
    print(f"Task added successfully (ID: {task_id})")


def list_tasks(status) -> None:
        statuses = [task["status"] for task in tasks.values()]
        if not tasks:
                return print("Please add new tasks")
        elif status not in statuses:
                return print(f"No tasks with status {status}")
        else:
                match status:
                        case None:
                                for i in sorted(tasks, key=lambda x: int(x)):
                                                print(f"{i} : {tasks[i]['description']}")
                        case "to-do":
                                for i in sorted(tasks, key=lambda x: int(x)):
                                        if tasks[i]['status'] == "to-do":
                                                print(f"{i} : {tasks[i]['description']}")
                        case "in-progress":
                                for i in sorted(tasks, key=lambda x: int(x)):
                                        if tasks[i]['status'] == "in-progress":
                                                print(f"{i} : {tasks[i]['description']}")
                        case "done":
                                for i in sorted(tasks, key=lambda x: int(x)):
                                        if tasks[i]['status'] == "done":
                                                print(f"{i} : {tasks[i]['description']}")

def update_task(task_id, description) ->None:
        if not tasks:
                print("Please add new tasks")
        elif task_id not in tasks:
                print(f"Task (ID: {task_id}) not in traker")
        else:
                tasks[task_id]['description'] = description
                with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
                print(f"Task updated successfully: {task_id}. {tasks[task_id]['description']}")

def delete_task(task_id)->None:
        id = str(task_id)
        if not tasks:
                print("Please add new tasks")
        elif id not in tasks:
                print(f"Task (ID: {id}) not in traker")
        else:
                des = tasks[id]['description']
                del tasks[id]
                with open(file, "w") as f:
                        json.dump(tasks, f, indent=4)
                print(f"Task deleted successfully: {id}. {des}")

def mark_task(task_id, status)->None:
        id = str(task_id)
        if not tasks:
                print("Please add new tasks")
        elif id not in tasks:
                print(f"Task (ID: {id}) not in traker")
        else:
                if tasks[id]['status'] == status:
                        return print(f"Task {id} current status is {status}")
                else:
                        tasks[id]['status'] = status
                        with open(file, "w") as f:
                                json.dump(tasks, f, indent=4)
                        print(f"Task status updated successfully to {status}")
