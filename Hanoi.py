def towerOfHanoi(s, d, e, n):
    #s : source, d : destination, e : extra, n : number of disk
    #s에 있는 원반을 d를 거쳐 n-1개만큼 e로 이동
    #n번째 원반을 d로 이동
    #n-1개의 원반을 s를 거쳐 d로 이동
    if n<=0:
        return
    towerOfHanoi(s,e,d,n-1)
    print(f'{n}번 원반을 {s}에서 {d}로 옮깁니다.')
    towerOfHanoi(e,d,s,n-1)

towerOfHanoi('s','d','e',3)