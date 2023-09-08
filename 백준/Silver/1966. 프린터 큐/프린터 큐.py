from collections import deque


def print_order(N, M, imp):
    # q: (문서의 중요도, 해당 위치)로 큐에 저장
    q = deque([(importance, index) for index, importance in enumerate(imp)])
    count = 0

    while q:
        # 현재 Queue의 맨 앞 문서 확인
        curr = q.popleft()

        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있다면,

        # curr: 현재 처리 중인 항목이나 데이터
        # doc: 큐에 있는 다른 문서들 중 하나
        if any(curr[0] < doc[0] for doc in q):  # ~ <나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있다면>,
            q.append(curr)  # ~ 현재 문서를 Queue의 가장 뒤에 재배치
        else:  # 그렇지 않다면 문서를 인쇄
            count += 1
            if curr[1] == M:  # ~ <맨 앞 문서가 내가 찾던 문서인 경우>,
                return count


def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        imp = list(map(int, input().split()))
        print(print_order(N, M, imp))


if __name__ == "__main__":
    main()
