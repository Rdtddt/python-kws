class Character:
     def __init__(self, name, hp, strength):
          self.name=name
          self.hp=hp
          self.strength=strength
          print(f'캐릭터 {self.name}이 생성되었습니다. 체력은 {self.hp}, 힘은 {self.strength} 입니다.')
     def attack(self, other_character):
          print(f' {self.name}이(가) {other_character.name} 을(를) 공격합니다!')
          other_character.hp -= self.strength
     #def __del__(self):
          #print(f'{self.name}이(가) 게임에서 사라졌습니다.')
          #객체가 메모리 구조에서 사라질 때 호출
     def remove_from_game(self):
          print(f'{self.name}이 게임에서 사라졌습니다')

naymar = Character("Naymar", 300, 50)
son  = Character('son', 400, 100)

son.attack(naymar)
print(f'네이마르의 남은 체력은 {naymar.hp}입니다.')

naymar.attack(son)
print(f'손흥민의 남은 체력은 {son.hp}입니다.')

son.attack(naymar)
print(f'네이마르의 남은 체력은 {naymar.hp}입니다.')

if naymar.hp<=0:
     naymar.remove_from_game()
     
#! 소멸자 사용 시 주의사항
#소멸자(__del__)는 객체가 메모리에서 제거될 때 호출
#소멸자의 삭제 시점을 프로그래머가 명확하게 지정할 수 없음.
#파이썬의 garbage collection이 언제 동작할지 불분명
