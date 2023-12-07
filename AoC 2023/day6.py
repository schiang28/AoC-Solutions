time, distance = [49979494], [263153213781851]
ans = 1

for race in range(len(time)):
    ways = 0
    for t in range(1, time[race]):
        if t * (time[race]-t) > distance[race]:
            ways+=1
    ans *= ways

print(ans)