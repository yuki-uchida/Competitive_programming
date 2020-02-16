N = input()
papers = input().split(" ")
papers = [int(n) for n in papers]
accepted = True
for paper in papers:
    if (paper % 2 == 0):
        if (paper % 3 == 0) | (paper % 5 == 0):
            pass
        else:
            accepted = False
    else:
        pass

if accepted:
    print("APPROVED")
else:
    print("DENIED")
