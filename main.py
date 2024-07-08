todos = []

def add_todo(task):
  todos.append(task)
  print(f"Added '{task}' to the to-do list.")

def view_todos():
  if not todos:
    print("The to-do list is empty.")
  else:
    print("To-do list:")
    for index, task in enumerate(todos):
      print(f"{index+1}. {task}")

def remove_todo(index):
  if 0 <= index < len(todos):
    removed_task = todos.pop(index)
    print(f"Removed '{removed_task}' from the to-do list.")
  else:
    print("Invalid index.")

while True:
  print("\nChoose an action:")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Remove a task")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    task = input("Enter the task: ")
    add_todo(task)
  elif choice == '2':
    view_todos()
  elif choice == '3':
    view_todos()
    if todos:
      index = int(input("Enter the index of the task to remove: ")) - 1
      remove_todo(index)
  elif choice == '4':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")