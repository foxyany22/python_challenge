length = int(input())
size = length * length

res = []
a = []

n = length - 1
count = length - 1
temp = 2

for i in range(1, length+1):
  a.append(i)

res.append(a)
a = []

for i in range(length+1, size+1):
  if count != 0:
    a.append(i)
    count -= 1
  else:
    temp -= 1
    res.append(a)
    a = []
    a.append(i)
    if temp == 0 and n > 0:
      temp = 2
      n -= 1
    count = n - 1
res.append(a)

print(res)

# 0 - left
# 1 - down 
# 2 - right
# 3 - up
direction = 0
a = 0
left = 0
leftLR = 0
saveLR = 0
down = 1
saveDown = 1
downLR = length
right = length - 1
rightLR = length - 2
saveRightLR = length - 2
saveUp = length - 2
up = length - 2
upLR = 0

out = []
tmp = []

for i in range(len(res)):
  for j in range(len(res[i])):
    print(i, j, res[i][j], end='\t\t')
  print('')

for i in range(length):
  for j in range(length+1):
    tmp.append(0)
  out.append(tmp)
  tmp = []

for i in range(len(res)):
  for j in range(len(res[i])):
    if a != i:
      direction += 1
      if direction == 4:
        left += 1
        saveDown += 1
        down = saveDown
        saveLR += 1
        leftLR = saveLR
        right -= 1
        saveUp -= 1
        up = saveUp
        upLR += 1
        downLR -= 1
        saveRightLR -= 1
        rightLR = saveRightLR
        direction = 0
      a = i

    if direction == 0:
      out[left][leftLR] = res[i][j]
      leftLR += 1
    elif direction == 1:
      out[down][downLR] = res[i][j]
      down += 1
    elif direction == 2:
      out[right][rightLR] = res[i][j]
      rightLR -= 1
    elif direction == 3:
      out[up][upLR] = res[i][j]
      up -= 1

print(out)

for i in range(len(out)):
  for j in range(len(out[i])):
    if out[i][j] != 0:
      print(out[i][j], end=' ')
  print('')