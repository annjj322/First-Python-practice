# 데이터를 파일형태로 저장, 남이 pickle을 이용해서 사용할 수 있다.

import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile's data -> save in file
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file's data -> load to profile
print(profile)
profile_file.close() # dictionary 내용을 적어주지 않았는데 loading해와서 profile에 저장한것