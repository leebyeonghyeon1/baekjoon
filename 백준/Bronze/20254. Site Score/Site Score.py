UR, TR, UO, TO= map(int,input().split())
if 0 < UR <= TR <= 120 and 0 < UO <= TO <= 1000: pass
print(56*UR + 24*TR + 14*UO + 6*TO)