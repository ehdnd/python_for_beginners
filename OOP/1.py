class Dog:
  #name, age, breed 정보 필요 // 자동으로 실행
  #이걸로 class 기본값 세팅 !
  def __init__(self, name, breed, age):
    self.name = name
    self.age = age
    self.breed = breed


class Puppy(Dog):
  #puppy여도 dog의 init method 실행함 -> 활용하기
  #age는 정해져있으니 name, breed만 알고싶음
  #밖에서 가져온 name, breed 넣어 >> Dog__init__으로 전달, w/나이가 5
  def __init__(self, name, breed):
    super().__init__(name, breed, 0.1)
    self.aggressive = False #Puppy 만의 properties

  def bark(self):
    print("Woof!")


class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(name, breed, 5)
    self.aggressive = True
  
  def bark(self):
    print("RRRR!")


#age 에 대한 내용은 제외하고 제공중
#ruffus와 bibi는 객체임 (instance라고 부른다)
ruffus = Puppy(name="Ruffus", breed="dal")

bibi = GuardDog(name="Bibi", breed="sig")

print(ruffus.name, ruffus.age)
print(bibi.name)