def valid(voice):
    if not voice.count("h") == 1:
        raise ValueError("invalid input")


say = input()
valid(say)
hear = input()
valid(hear)
# 말하는 길이가 더 길어야 병원에 갈 수 있다.
print("go" if say.count("a") >= hear.count("a") else "no")
