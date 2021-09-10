#url = "http://google.com"
url = "http://youtube.com"

site = url.replace("http://","")
print(site)

number = int(site.index("."))
site = site.replace(site[number:],"")

password_number = len(site)
e_number = site.count("e")
three_word= site[0:3]



#규칙3
print(f"생성된 {url} 사이트의 비밀번호 : {three_word}{password_number}{e_number}!")

#solution
#my_str = my_str[:my_str.index(".")] 점 뒤로는 삭제==점 앞까지만 슬라이싱
