def solution(phone_book):
    num = len(phone_book)
    for i in range(num-1):
        phone = phone_book[i]
        for j in range(i+1, num):
            n_phone = phone_book[j]
            if phone.startswith(n_phone) or n_phone.startswith(phone):
                return False
    answer = True
    return answer
