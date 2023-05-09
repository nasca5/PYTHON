
# class가 필요한 이유
# 1. class : 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면과 같다. 이러한 class로 만든 피조물을 object(객체)라고 한다.
# 2. class로 만든 object들은 각자 고유한 성격을 가진다는 특징이 있다.
# 3. class : 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면과 같다. 이러한 class로 만든 피조물을 object(객체)라고 한다.
# 2. class로 만든 object들은 각자 고유한 성격을 가진다는 특징이 있다.
# 3. class : 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면과 같다. 이러한 class로 만든 피조물을 object(객체)라고 한다.
# 2. class로 만든 object들은 각자 고유한 성격을 가진다는 특징이 있다. 즉 동일한 class로 만든 객체들이라고 할지라도 서로 전혀 영향을 주지 않는다.
# 3. class의 결괏값을 돌려받은 변수는 object가 된다.
# 4. 또한 class로 만든 object는 인스턴스라고도 한다. 만약 cookie()라는 class로 a라는 객체를 만든다면 a는 객체이면서
# cookie()의 인스턴스이기도 하다.
# 5. 이 말인 즉슨 인스턴스는 특정 object가 어떤 class의 object인지를 관계 위주로 설명할 때 사용되는 단어이다.
# 6. 즉 'a는 객체'라고 표현하는 것도 맞고, 'a는 cookie() class의 인스턴스'라고 설명하는 것도 옳은 설명이다.
# 7. class를 만들때에는 무작정 만드는 것보다 미리 이 class가 만든 객체가 어떤 식으로 동작하게 될 것인지를
# 미리 구상한 후에 구상한 기능들을 하나씩 해결하면서 만드는 것이 좋다.

# 8. 사칙연산을 하는 Fourcal class 만들기
# 순서 : 1. 사칙연산을 하기 위해 두 숫자를 입력받음  -> setdata 메소드
#        2. 더하기 연산 -> add 메소드
#        3. 빼기 연산 -> sub 메소드
#        4. 곱하기 연산 -> mul 메소드
#        5. 나누기 연산 -> div 메소드
# class 안에서 구현된 함수는 메소드(method)라고도 부른다.
# 메소드에 첫 번째로 전달되는 self에는 메소드를 호출한 object(아래에선 a)가 자동으로 전달된다.
# 파이썬에서 메소드의 첫 번째 매개 변수 이름은 관례적으로 self를 사용한다. object를 호출할 때 호출한 object 자신이 전달되기 때문에 self라고 하는 것 같다.
# 잘 사용하지는 않지만 class를 통해 메소드를 호출하는 것도 가능하다.
# classname.메소드 형태로 호출할 때는 object를 반드시 첫 번째 매개변수인 self에 전달해주어야 한다. object를 통해 전달할 때는 self는 생략한다.


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)
b = FourCal(3, 7)

a.setdata(4, 2)
b.setdata(3, 7)

print(id(a.first))
print(id(b.first))

# 위의 object a와 b는 서로 영향을 주지 않고 고유의 성향을 가지므로 object a에서 first의 값에 4를 주고
#  object b에서 first의 값에 3을 줘도 a나 b의 값이 변경되거나 하지 않는다.
# 객체끼리는 서로 완전히 독립적인 존재이다.
# 이는 변수의 주소값을 확인할 수 있는 id() 함수를 통해 쉽게 확인해볼 수 있는데, id(a.first) id(b.first)의 주소값은 다르다는 것을 확인해볼 수 있다.

# 위의 FourCal() class의 a 인스턴스에 setdata 메소드를 수행하지 않고 바로 a 인스턴스에 add 메소드를 수행하면 a 인스턴스의 변수가
# 생성되지 않기 때문에 오류가 난다.
# 이렇게 인스턴스에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메소드를 호출하여 초깃값을 설정하기보다는 생성자(Constructor)를 구현하는 것이 좋다.
# 생성자(Constructor) : object가 생성될 때 자동으로 호출되는 메소드를 의미한다.
# 파이썬 메소드 이름으로 __init__을 사용하면 이 메소드는 생성자가 된다.
# 하지만 생성자(Contstructor)를 구현하여도 생성자(Contstructor)의 매개변수 first와 second에 해당하는 값이 전달되지 않으면 오류가 발생하기 때문에
# 이러한 오류를 예방하려면 first와 second 변수의 값을 전달하면서 객체를 생성해야 한다. -> ex) a = FourCal(4,2)

# class의 상속(inheritance) : class에서도 상속의 개념이 가능하다.
# 어떤 class를 만들 때 다른 class의 기능을 물려받을 수 있게 만드는 것이 가능하다는 뜻이다.
# 보통 상속은 기존 class를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
# 물론 개인이 작성한 class라면 class를 직접 수정할수도 있겠지만
# 라이브러리나 프레임워크의 class를 사용할 때 수정이 허용되지 않는 상황이 있기 때문에, 이럴때는 상속을 사용해야 한다.

# FourCal() class를 이용하여 a의 b제곱을 구하는 MoreFourCal() class 만들기

class MoreFourCal(FourCal) :
  def pow(self) :
    result = self.first ** self.second
    return result

a = MoreFourCal(4, 2)
print('안녕하세요')

# MoreFourCal() class는 FourCal() class를 상속했으므로 FourCal() class의 모든 기능을 사용할 수 있어야 한다.
# 위의 예시처럼 상속은 기존 class는 그대로 유지한 채로 class의 기능을 확장시킬 때 주로 사용한다.

# 메소드 오버라이딩(overriding)
# 메소드 오버라이딩은 부모 class에 있는 메소드를 동일한 이름으로 다시 만드는 것을 의미한다.
class SafeFourCal(FourCal) :
  def div(self) :
    if self.second == 0 :
      return 0;
    else :
      return self.first / self.second

a = SafeFourCal(4, 0)

print(a.div())

# class 변수 : object 변수는 다른 객체들에게 영향을 받지 않지만, class 변수는 class로 만든 모든 객체에 공유된다는 특징이 있다.

class Family :
  lastname = '강'

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = 'Kang'

print(a.lastname)
print(b.lastname)

# 위의 예시를 보면 Family class의 변수의 값을 바꾸면 a.lastname과 b.lastname의  값이 모두 바뀐다는 것을 알 수 있다.
# 이처럼 class 변수는 class로 만든 모든 object에 공유된다는 사실을 알 수 있다.

# 모듈(module) : 모듈이란 함수나 변수 class를 모아 놓은 파일이라고 할 수 있다. 보통 파이썬으로 프로그래밍을 하면 모듈을 굉장히 많이 사용하게 된다.
# 모듈 만들기
import test

print(test.add(4, 3))

# 위의 예시처럼 모듈을 사용하려면 import 모듈 이름을 하면 된다. 내가 만든 모듈을 이용하고 싶으면 만들어놓은 모듈이 같은 directory 내에 있어야 한다.
from test4 import add

print(add(3, 5))

# 만약 모듈 자체가 아니라 모듈에 있는 함수만 불러오고 싶다면 위의 예시처럼 하면 된다.
# 만약 모듈을 직접 실행하게 되면 모듈 안에 출력문이 있다면 바로 출력되어버리는데, 이때 모듈에다가 아래의 문장들을 추가하면 그러한 오류를 막을 수 있다.
if __name__ == "__main__" :
    