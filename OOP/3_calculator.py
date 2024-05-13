class FourCal:
  # 객체 생성과 동시에 __init__ 실행됨
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    result = self.first + self.second
    return result

  def mul(self):
    result = self.first * self.second
    return result

  def sub(self):
    result = self.first - self.second
    return result

  def div(self):
    result = self.first / self.second
    return result

class MoreFourCal(FourCal):
  def pow(self):
    result = self.first ** self.second
    return result

class SafeFourCal(FourCal):
  #'div' method overriding, 덮어쓰기
  def div(self):
    if self.second == 0:
      return "'second' can't be '0'..."
    else:
      return self.first / self.second

a = SafeFourCal(2, 0)
print(a.div())