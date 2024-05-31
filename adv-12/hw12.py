from collections import deque
snack_queue=deque()
snack_queue.append('無名氏')
snack_queue.append('無名氏2')
snack_queue.append('無名氏3')
print(f'初始數列:{snack_queue}')
first_student=snack_queue.popleft()
print(f'{first_student}已經購買點心並離開數列')
print(f'現在的隊列:{snack_queue}')

