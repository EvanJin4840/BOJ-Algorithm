# 인공지능 시계 문제

hour, minute, second = map(int, input().split())
required_seconds = int(input())

total_seconds = hour * 3600 + minute * 60 + second + required_seconds

hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

if(hour >= 24):
    hour = hour % 24

print(hour, minute, second)