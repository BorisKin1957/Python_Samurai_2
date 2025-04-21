

st1 = set(map(int, input().split()))
st2 = set(map(int, input().split()))

st1 -= st2

print(*sorted(st1))