

lst1 = set(map(int, input().split()))
lst2 = set(map(int, input().split()))

lst1 -= lst2

print(*sorted(lst1))