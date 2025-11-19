from .core.core_functions import add_task, list_tasks, update_task, delete_task, mark_task
import argparse

def main():
    
    
    parser = argparse.ArgumentParser(description="Task Tracker CLI (ArgeParse implementation)")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs=argparse.REMAINDER, help="Task description")

    list_parser = subparsers.add_parser("list", help="list tasks by status [to-do, in-progress, done]")
    list_sub = list_parser.add_subparsers(dest="list_cmd")

    list_parser.set_defaults(list_cmd="all")
    
    list_sub.add_parser("to-do", help="list tasks not started")
    list_sub.add_parser("in-progress", help="list tasks in progres")
    list_sub.add_parser("done", help="list completed tasks")

    update_parser = subparsers.add_parser("update", help="update existing task")
    update_parser.add_argument("update", nargs="+", help="update task description")
    
    delete_parser = subparsers.add_parser("delete", help="delete existing task")
    delete_parser.add_argument("id", help="Task ID to delete")

    mark_p_parser = subparsers.add_parser("mark-in-progress", help="mark existing task as in-progress")
    mark_p_parser.add_argument("id", help="Task ID to mark")
    
    mark_d_parser = subparsers.add_parser("mark-done", help="mark existing task as done")
    mark_d_parser.add_argument("id", help="Task ID to mark")

    args = parser.parse_args()

    match args.command:
            case "add":
                add_task(" ".join(args.description))
            case "list":
                match args.list_cmd:
                    case "all":
                          list_tasks(status = None)
                    case "to-do":
                          list_tasks(args.list_cmd)
                    case "in-progress":
                          list_tasks(args.list_cmd)
                    case "done":
                          list_tasks(args.list_cmd)
            case "update":
                try:
                    task_id = int(args.update[0])
                    description = " ".join(args.update[1:])
                    update_task(str(task_id), description)
                except ValueError :
                     print("Invalid input: usage: update [-task id] [-task description]")
            case "delete":
                try:
                    delete_task(int(args.id))
                except ValueError:
                     print("Invalid input: usage: delete [-task id]")
            case "mark-in-progress":
                try:
                    status = "in-progress"
                    mark_task(int(args.id), status)
                except ValueError:
                     print("Invalid input: usage: mark-in-progress [-task id]")
            case "mark-done":
                try:
                    status = "done"
                    mark_task(int(args.id), status)
                except ValueError:
                    print("Invalid input: usage: mark-done [-task id]")
            case _:
                parser.print_help()



