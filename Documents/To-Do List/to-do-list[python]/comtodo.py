todo_list = []

# 투두 항목 추가
def add_todo(task):
    todo_list.append({"task": task, "done": False})
    print(f"투두 항목 '{task}' 추가됨")

# 투두 항목 완료 표시
def mark_done(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["done"] = True
        print(f"투두 항목 '{todo_list[index]['task']}' 완료 표시됨")
    else:
        print("유효하지 않은 인덱스입니다.")

# 투두 항목 삭제
def delete_todo(index):
    if 0 <= index < len(todo_list):
        deleted_task = todo_list.pop(index)
        print(f"투두 항목 '{deleted_task['task']}' 삭제됨")
    else:
        print("유효하지 않은 인덱스입니다.")

# 투두 리스트 출력
def print_todo_list():
    print("투두 리스트:")
    for i, item in enumerate(todo_list):
        status = "[X]" if item["done"] else "[ ]"
        print(f"{i+1}. {status} {item['task']}")

# 메뉴 표시 및 사용자 입력 처리
while True:
    print("\n1. 투두 항목 추가")
    print("2. 투두 항목 완료 표시")
    print("3. 투두 항목 삭제")
    print("4. 투두 리스트 출력")
    print("5. 종료")

    choice = input("선택: ")

    if choice == "1":
        task = input("투두 항목 입력: ")
        add_todo(task)
    elif choice == "2":
        index = int(input("완료 표시할 투두 항목 인덱스 입력: ")) - 1
        mark_done(index)
    elif choice == "3":
        index = int(input("삭제할 투두 항목 인덱스 입력: ")) - 1
        delete_todo(index)
    elif choice == "4":
        print_todo_list()
    elif choice == "5":
        break
    else:
        print("유효하지 않은 선택입니다.")