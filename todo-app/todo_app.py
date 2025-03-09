import click
import json
import os

TODO_FILE = "todo.json"

def load_todo():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_task(task):
    with open(TODO_FILE, "w") as file:
        json.dump(task, file, indent=4)

@click.group()
def cli():
    pass

@click.command()
@click.argument("task")
def add(task):
    tasks = load_todo()
    tasks.append({"task":task, "done":False})
    save_task(tasks)
    click.echo(f"Task added successfully {task}")

@click.command()
def list():
    tasks = load_todo()
    if not tasks:
        click.echo("No tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index},{task['task']}, [{status}]")

@click.command()
@click.argument("task_num", type=int)
def completed(task_num):
    tasks = load_todo()
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Task {task_num} marked as completed")
    else:    
        click.echo(f"Invalid task number {task_num}")

@click.command()
@click.argument("task_num", type=int)
def delete(task_num):
    tasks = load_todo()
    if 0 < task_num <= len(tasks):
        remove_task = tasks.pop(task_num-1)
        save_task(tasks)
        click.echo(f"The task {remove_task['task']} has been deleted")
    else:
        click.echo(f"Invalid task number {task_num}")


cli.add_command(add)
cli.add_command(completed)
cli.add_command(list)
cli.add_command(delete)

if __name__ == "__main__":
    cli()