score = input("輸入分數")
score = int(score)

if score >= 90:
    grade = "A"
elif score < 90 and score>=80:
    grade = "B"
elif score < 80 and score>=70:
    grade = "C"
elif score < 70 and score>=60:
    grade = "D"
else:
    grade = "F"
print(f"你的成績是{score}分，等級為{grade}")
