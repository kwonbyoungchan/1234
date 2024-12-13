#todo_list = []

#while True:
#    print("할 일 목록:")
#    for index, item in enumerate(todo_list): #enumerate() 함수는 각 반복 단계에서 (인덱스, 값)의 튜플을 반환
#        print(f"{index + 1}. {item}") #문자열 포맷팅.

#    print("\n무엇을 하시겠습니까?")
#    print("1. 할 일 추가")
#    print("2. 종료")

#    choice = input("선택하세요 (1, 2): ")

#    if choice == "1":
#        new_item = input("\n추가할 할 일을 입력하세요: ")
#        todo_list.append(new_item)
#        print(f"\n'{new_item}'이(가) 할 일 목록에 추가되었습니다.")

#    elif choice == "2":
#        print("프로그램을 종료합니다.")
#        break
#    else:
#        print("올바른 옵션을 선택하세요.")

########-------------------여기까지 가져온 코드입니다.----------##############
########-------------------본래 To-do-list 기능에 필요로 할만한 기능들을 추가해보았습니다.-----------------####################

# 날짜와 시간 처리를 위한 라이브러리를 임포트 시켰습니다.
from datetime import datetime, timedelta

# 할 일 목록과 기타 필요한 리스트를 빈칸으로  초기화시켰습니다.
todo_list = []

# 우선순위와 완료 여부를 나타내는 상태 딕셔너리,{}형태는 딕셔너리!
priority_dict = {1: '중요', 2: '보통', 3: '덜 중요'}

# 프로그램을 반복하는 반복문을 작성하였습니다.
while True:
    print("\n할 일 목록:")
    
    # 할 일 목록을 출력합니다. (우선순위와 완료 상태 포함)
    for index, item in enumerate(todo_list): 
        # todo_list를 순회하면서 인덱스와 항목을 가져옵니다.
        status = "완료" if item['done'] else "진행 중"  # 완료 여부에 따라 상태를 결정합니다.
      
        # 할 일을 출력합니다. (우선순위, 마감일, 상태 포함)
        print(f"{index + 1}. {item['task']} - 우선순위: {priority_dict.get(item['priority'], '없음')} - 마감일: {item['deadline']} - 상태: {status}")
    
    # 사용자에게 선택 할 선택지를 Print 함수로 보여줍니다.
    print("\n무엇을 하시겠습니까?")
    print("1. 할 일 추가")
    print("2. 우선순위 설정")
    print("3. 완료된 일 체크")
    print("4. 할 일 검색")
    print("5. 완료된 일 삭제")
    print("6. 주간 할 일 요약")
    print("7. 종료")
    
    # 사용자로부터 선택지를 입력받는 input함수를 사용해서 입력받습니다.
    choice = input("선택하세요 (1, 2, 3, 4, 5, 6, 7): ") 

    if choice == "1":
        # 할 일 추가/ 새로운 할 일을 입력 받습니다.
        new_item = input("\n추가할 할 일을 입력하세요: ") 

        # 우선순위 설정/ 우선순위를 입력 받습니다.
        priority = int(input("우선순위를 선택하세요 (1: 중요, 2: 보통, 3: 덜 중요): "))  

        # 마감 날짜 설정/ 마감 날짜를 입력 받습니다.
        deadline = input("마감 날짜를 입력하세요 (YYYY-MM-DD): ")  
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")  # 입력된 날짜를 datetime 객체로 변환합니다.

        # 할 일 추가/할 일을 목록에 추가합니다.
        todo_list.append({"task": new_item, "priority": priority, "deadline": deadline_date, "done": False}) 
        # 할 일이 추가되었다는 메시지 출력합니다.
        print(f"'{new_item}'이(가) 할 일 목록에 추가되었습니다.")  

    elif choice == "2":
        # 우선순위 설정/# 우선순위를 변경할 할 일 번호 입력받습니다.
        index = int(input("우선순위를 변경할 할 일 번호를 입력하세요: ")) - 1 
        if index < len(todo_list):
            # if함수를 사용해서 우선순위를 변경하는 파트입니다.
            priority = int(input("우선순위를 선택하세요 (1: 중요, 2: 보통, 3: 덜 중요): "))
            # 선택된 할 일의 우선순위를 변경합니다.
            todo_list[index]["priority"] = priority 
            # 위에서 변경된 우선순위를 출력합니다.
            print(f"'{todo_list[index]['task']}'의 우선순위가 변경되었습니다.")  
        # 번호가 유효하지 않으면 에러 메세지를 출력합니다.
        else:
            print("유효하지 않은 번호입니다.") 

    elif choice == "3":
        # 완료된 일 체크
        # 완료 처리할 할 일 번호를 입력받습니다.
        index = int(input("완료할 할 일 번호를 입력하세요: ")) - 1  
        if index < len(todo_list):
            # 해당 할 일의 상태를 완료로 변경합니다.
            todo_list[index]["done"] = True 
            # 완료된 할 일 메시지 출력
            print(f"'{todo_list[index]['task']}'이(가) 완료되었습니다.")  
        # 번호가 유효하지 않으면 에러 메세지를 출력합니다.
        else:
            print("유효하지 않은 번호입니다.")  

    elif choice == "4":
        # 할 일 검색 기능
        # 검색 할 키워드를 입력받습니다.
        search_term = input("검색할 할 일의 키워드를 입력하세요: ") 
        # todo_list에서 키워드가 포함된 할 일을 찾습니다.
        results = [item for item in todo_list if search_term in item['task']]  
        print("검색 결과:")
        for item in results:
            # 검색된 할 일 목록 출력
            print(f"{item['task']} - 우선순위: {priority_dict.get(item['priority'], '없음')} - 마감일: {item['deadline']} - 상태: {'완료' if item['done'] else '진행 중'}")

    elif choice == "5":
        # 완료된 일 삭제
        # 완료된 일이 있으면 목록에서 제거합ㄴ다.
        todo_list = [item for item in todo_list if not item["done"]] 
        # 완료된 일이 삭제 되었다는 메세지를 출력합니다.
        print("완료된 할 일이 삭제되었습니다.") 

    elif choice == "6":
        # 주간 할 일 요약
        # 이번 주의 시작 날짜를 계산하는 식입니다.
        start_of_week = datetime.now() - timedelta(days=datetime.now().weekday()) 
        # 이번 주의 끝 날짜를 계산하는 식입니다.
        end_of_week = start_of_week + timedelta(days=6)  
        

        # 주간 할 일 목록을 필터링 합니다.
        weekly_tasks = [item for item in todo_list if start_of_week <= item["deadline"] <= end_of_week] 
        print("이번 주 할 일 목록:")
        for task in weekly_tasks:
            # 이번 주 할 일 목록을 출력합니다.
            print(f"{task['task']} - 우선순위: {priority_dict.get(task['priority'], '없음')} - 마감일: {task['deadline']} - 상태: {'완료' if task['done'] else '진행 중'}")

    elif choice == "7":
        #7을 입력하면 프로그램을 종료를 출력합니다.
        print("프로그램을 종료합니다.") 
        # 무한 루프를 종료하기 위해 사용했습니다.
        break  
    
    # 올바르지 않은 선택을 했을 때 에러메세지를 출력합니다.
    else:
        print("올바른 옵션을 선택하세요.")  

