my_set = {1,2,3,3,3}
print(my_set) # 중복을 허용하지 않음

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 (java and python both of them)
print(java & python)
print(java.intersection(python))

# 합집합 (java or python)
print(java | python)
print(java.union(python))

# 차집합 (java, not python)
print(java - python)
print(java.difference(python))

# 집합요소 추가 
python.add("김태호")
print(python)

# 집합요소 제거
java.remove("김태호")
print(java)