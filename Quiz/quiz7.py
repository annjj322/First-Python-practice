for x in range(1,51):
    report_file = open(f"{x}주차.txt", "w", encoding="utf8")
    report_file.write(f"- {x} 주차 주간보고- \n")
    report_file.write(f"- 부서 : \n")
    report_file.write(f"- 이름 : \n")
    report_file.write(f"- 업무 요약 : \n")
report_file.close()

# for i in range(1,51):
#   with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#       report_file.write(f"- {i} 주차 주간보고-\n")
#       report_file.write("부서 :\n")
#       report_file.write("이름 :\n")
#       report_file.write("업무 요약 :\n")
