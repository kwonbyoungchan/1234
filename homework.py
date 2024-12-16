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

# 색상 정의
RESET = "\033[0m"  # 기본 색상으로 초기화
BOLD = "\033[1m"   # 굵은 글씨
RED = "\033[31m"   # 빨간색
GREEN = "\033[32m" # 초록색
YELLOW = "\033[33m" # 노란색
CYAN = "\033[36m"  # 청록색

# 날짜와 시간 처리를 위한 라이브러리 datetime과 timedelta를 임포트합니다.
from datetime import datetime, timedelta

# 할 일 목록을 저장할 리스트를 빈 리스트로 초기화합니다.
todo_list = []

# 우선순위를 표현하기 위해 딕셔너리를 사용합니다.
# priority_dict는 숫자 키를 우선순위 문자열에 대응시키며, 색상 코드와 함께 우선순위를 표시합니다.
priority_dict = {1: f"{RED}중요{RESET}", 2: f"{YELLOW}보통{RESET}", 3: f"{CYAN}덜 중요{RESET}"}

# 프로그램을 무한히 실행하기 위한 while 반복문을 사용합니다.
while True:
    # 할 일 목록을 출력합니다. enumerate 함수는 목록에서 인덱스와 항목을 동시에 가져옵니다.
    print(f"\n{BOLD}{CYAN}할 일 목록:{RESET}")
    for index, item in enumerate(todo_list):
        # 완료 여부를 확인하여 상태를 "완료" 또는 "진행 중"으로 설정합니다.
        # status는 삼항 연산자를 사용하여 True일 때 '완료', False일 때 '진행 중'을 설정합니다.
        status = f"{GREEN}완료{RESET}" if item['done'] else f"{RED}진행 중{RESET}"
        # 항목의 할 일 내용, 우선순위, 마감일, 상태를 출력합니다.
        # 우선순위는 priority_dict에서 해당 우선순위에 맞는 색상과 함께 출력됩니다.
        print(f"{index + 1}. {item['task']} - 우선순위: {priority_dict.get(item['priority'], '없음')} - 마감일: {item['deadline'].strftime('%Y-%m-%d')} - 상태: {status}")
    
    # 메뉴를 출력합니다. 각 옵션에는 색상이 추가되어 있습니다.
    print(f"\n{BOLD}무엇을 하시겠습니까?{RESET}")
    print(f"{CYAN}1. 할 일 추가{RESET}")
    print(f"{YELLOW}2. 우선순위 설정{RESET}")
    print(f"{GREEN}3. 완료된 일 체크{RESET}")
    print(f"{CYAN}4. 할 일 검색{RESET}")
    print(f"{RED}5. 완료된 일 삭제{RESET}")
    print(f"{GREEN}6. 주간 할 일 요약{RESET}")
    print(f"{RED}7. 종료{RESET}")
    
    # 사용자로부터 메뉴 선택을 받습니다. input() 함수로 선택을 입력받습니다.
    choice = input("선택하세요 (1, 2, 3, 4, 5, 6, 7): ")

    # 사용자가 1을 선택한 경우, 새로운 할 일을 추가합니다.
    if choice == "1":
        # input() 함수로 할 일 이름을 입력받습니다.
        new_item = input("\n추가할 할 일을 입력하세요: ")
        # 우선순위를 선택받습니다. int() 함수로 숫자로 변환합니다.
        priority = int(input("우선순위를 선택하세요 (1: 중요, 2: 보통, 3: 덜 중요): "))
        # 마감 날짜를 입력받고, datetime.strptime() 함수를 사용해 문자열을 datetime 객체로 변환합니다.
        # strptime()은 주어진 포맷("%Y-%m-%d")에 맞춰 문자열을 datetime 객체로 파싱합니다.
        deadline = input("마감 날짜를 입력하세요 (YYYY-MM-DD): ")
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        # 새로운 할 일을 딕셔너리로 구성하여 todo_list에 추가합니다.
        todo_list.append({"task": new_item, "priority": priority, "deadline": deadline_date, "done": False})
        print(f"{GREEN}'{new_item}'이(가) 할 일 목록에 추가되었습니다.{RESET}")

    # 사용자가 2를 선택한 경우, 특정 할 일의 우선순위를 변경합니다.
    elif choice == "2":
        # 우선순위를 변경할 할 일 번호를 입력받습니다. 1을 빼서 0부터 시작하도록 조정합니다.
        index = int(input("우선순위를 변경할 할 일 번호를 입력하세요: ")) - 1
        # index가 유효한 범위 내에 있는지 확인합니다.
        if index < len(todo_list):
            # 새로운 우선순위를 선택받고, 해당 항목에 적용합니다.
            priority = int(input("우선순위를 선택하세요 (1: 중요, 2: 보통, 3: 덜 중요): "))
            todo_list[index]["priority"] = priority
            print(f"{CYAN}'{todo_list[index]['task']}'의 우선순위가 변경되었습니다.{RESET}")
        else:
            print(f"{RED}유효하지 않은 번호입니다.{RESET}")

    # 사용자가 3을 선택한 경우, 특정 할 일을 완료로 표시합니다.
    elif choice == "3":
        # 완료할 할 일 번호를 입력받습니다. 1을 빼서 0부터 시작하도록 조정합니다.
        index = int(input("완료할 할 일 번호를 입력하세요: ")) - 1
        # index가 유효한지 검사하고, 완료 상태를 True로 변경합니다.
        if index < len(todo_list):
            todo_list[index]["done"] = True
            print(f"{GREEN}'{todo_list[index]['task']}'이(가) 완료되었습니다.{RESET}")
        else:
            print(f"{RED}유효하지 않은 번호입니다.{RESET}")

    # 사용자가 4를 선택한 경우, 할 일을 검색합니다.
    elif choice == "4":
        # 검색할 키워드를 입력받습니다.
        search_term = input("검색할 할 일의 키워드를 입력하세요: ")
        # list comprehension을 사용하여 할 일 목록에서 검색어가 포함된 항목을 필터링합니다.
        results = [item for item in todo_list if search_term in item['task']]
        print(f"{CYAN}검색 결과:{RESET}")
        # 검색 결과를 출력합니다.
        for item in results:
            # 각 항목의 할 일 내용, 우선순위, 마감일, 상태를 출력합니다.
            print(f"{item['task']} - 우선순위: {priority_dict.get(item['priority'], '없음')} - 마감일: {item['deadline'].strftime('%Y-%m-%d')} - 상태: {'완료' if item['done'] else '진행 중'}")

    # 사용자가 5를 선택한 경우, 완료된 할 일을 삭제합니다.
    elif choice == "5":
        # 완료된 항목을 삭제하기 위해 리스트를 필터링합니다.
        todo_list = [item for item in todo_list if not item["done"]]
        print(f"{RED}완료된 할 일이 삭제되었습니다.{RESET}")

    # 사용자가 6을 선택한 경우, 주간 할 일 목록을 요약합니다.
    elif choice == "6":
        # 이번 주의 시작 날짜 (월요일)를 구합니다.
        start_of_week = datetime.now() - timedelta(days=datetime.now().weekday())
        # 이번 주의 끝 날짜 (일요일)를 구합니다.
        end_of_week = start_of_week + timedelta(days=6)
        # 주간 할 일 목록을 필터링합니다.
        weekly_tasks = [item for item in todo_list if start_of_week <= item["deadline"] <= end_of_week]
        print(f"{BOLD}{CYAN}이번 주 할 일 목록:{RESET}")
        # 주간 할 일 목록을 출력합니다.
        for task in weekly_tasks:
            print(f"{task['task']} - 우선순위: {priority_dict.get(task['priority'], '없음')} - 마감일: {task['deadline'].strftime('%Y-%m-%d')} - 상태: {'완료' if task['done'] else '진행 중'}")

    # 사용자가 7을 선택한 경우, 프로그램을 종료합니다.
    elif choice == "7":
        print(f"{RED}프로그램을 종료합니다.{RESET}")
        break
    
    # 잘못된 선택을 처리하기 위한 오류 메시지 출력
    else:
        print(f"{RED}올바른 옵션을 선택하세요.{RESET}")

