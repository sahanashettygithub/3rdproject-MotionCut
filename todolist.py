def main():
    tasks =[]
    while True:
        print("\n===== To-Do list =====")
        print("1.add task")
        print("2.show tasks")
        print("3.mark task as done")
        print("4.exit")

        choice = input("enter the your choice:")
        if choice =='1':
            print()
            n_tasks=int(input("how many tasks you want to add :"))
            for i in range(n_tasks):
                task = input("enter the task:")
                tasks.append({"task":task,"done":False})
                print("task added!")

        elif choice =='2':
            print("\ntasks:")
            for index,task in enumerate(tasks):
                status ="done" if task["done"] else "not done"
                print(f"{index+1}.{task['task']}-{status}")
        elif choice =='3':
            task_index=int(input("enter the task number to mark as done:"))-1
            if 0 <= task_index <len(tasks):
                tasks[task_index]["done"]=True
                print("task marked as done!")
            else:
                print("invalid task number.")
        elif choice =='4':
            print("exiting the To-do list.")
            break
        else:
            print("invalid choice.please try again.")

if __name__ =="__main__":
    main()


