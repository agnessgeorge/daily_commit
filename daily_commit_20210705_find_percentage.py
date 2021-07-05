if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        full = raw_input().split()
        name = full[0]
        scores = list(full[1:])
        student_marks[name] = scores
    query_name = raw_input()
    sum = float(0)
    for x in student_marks[query_name]:
        sum += float(x)
    avg = float(sum/3)
    print("{:.2f}".format(avg))