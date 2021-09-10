site = "http://naver.com"

site = site.replace("http://","")
print(site)

number = int(site.index("."))
site = site.replace(site[number:],"")

password_number = len(site)
e_number = site.count("e")
three_word= site[0:3]



#규칙3
print(f"생성된 비밀번호 : {three_word}{password_number}{e_number}!")