def test(a,b):
    for i in range(len(a)):
      if a[i] == b[i]:
          score += 1
      else:
        score = 0
    print(score)
