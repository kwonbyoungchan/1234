todo_list = []

while True:
    print("할 일 목록:")
    for index, item in enumerate(todo_list): #enumerate() 함수는 각 반복 단계에서 (인덱스, 값)의 튜플을 반환
        print(f"{index + 1}. {item}") #문자열 포맷팅.

    print("\n무엇을 하시겠습니까?")
    print("1. 할 일 추가")
    print("2. 종료")

    choice = input("선택하세요 (1, 2): ")

    if choice == "1":
        new_item = input("\n추가할 할 일을 입력하세요: ")
        todo_list.append(new_item)
        print(f"\n'{new_item}'이(가) 할 일 목록에 추가되었습니다.")

    elif choice == "2":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 옵션을 선택하세요.")

########-------------------여기까지 가져온 코드입니다.----------##############
