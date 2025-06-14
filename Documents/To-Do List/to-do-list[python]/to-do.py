print("""
==========TO-Do List==========
""")

to_do = []

while True:
    print("\033[0m\n 1 . 할 일 추가")
    print(" 2 . 할 일 삭제")
    print(" 3 . 완료 체크")
    print(" 4 . 할 일 전체 보기")
    print(" 5 . 종료")
    print()
    n = int(input("\n1 ~ 5 까지 중 하나를 선택 하십시오 >> "))
    print()
    print("=================================\n")
    if n == 5:
        print("\nTo-Do List를 종료합니다.")
        break
    elif n == 4:
        for i in range(len(to_do)):
            print(f"\033[94m{i+1}. {to_do[i]}")
    elif n == 3:
        num = int(input("몇 번 항목에 '완료'를 체크 하시겠습니까?   "))
        to_do[num-1] = f"✅{to_do[num-1]}"
    elif n == 2:
        num = int(input("몇 번 항목을 삭제하시겠습니까?   "))
        to_do.remove(to_do[num-1])
    elif n == 1:
        s = input("\n무슨 일을 추가 하시겠습니까?   ")
        to_do.append(s)
    else :
        print("\033[91m입력이 잘못 되었습니다")
        print("다시 입력해 주십시요")