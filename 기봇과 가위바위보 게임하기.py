import random


class Game:

        def __init__(self):
            self.items = '가위','바위','보'

            self.human_count = 0
            
            self.bot_count = 0

        def start(self):
            print('컴퓨터와의 가위-바위-보 게임을 시작하겠습니다.')

            while self.human_count < 3 and self.bot_count < 3:
                print('==============================================')
                human = input('가위, 바위, 보 중 하나를 입력하세요!:')

                bot = self.items[random.randint(0,2)]
                

                print('봇이 [',bot,']를 냈습니다.')
                if human == '가위':
                    if bot == '바위':
                        print('봇이 이겼네요..ㅜ.ㅜ.')
                        self.bot_count +=1
                    elif bot == '보':
                        print('당신이 이겼습니다!! :)')
                        self.human_count +=1
                    else:
                        print('비겼습니다.')
                                        
                elif human == '바위':
                    if bot == '바위':
                        print('비겼습니다.')
                    elif bot == '보':
                        print('봇이 이겼네요..ㅜ.ㅜ.')
                        self.bot_count +=1
                    else:
                        print('당신이 이겼습니다!! :)')
                        self.human_count +=1                              

                elif human == '보':
                    if bot == '바위':

                        
                        print('당신이 이겼습니다!! :)')
                        self.human_count +=1
                    elif bot == '보':
                        print('비겼습니다.')
                    else:
                        print('봇이 이겼네요..ㅜ.ㅜ.')
                        self.bot_count +=1                               

                else:
                    print('다시 입력하세요.')
        
            if self.bot_count >=3:
                    print('\n\n 봇이 먼저 세 판을 이겼군요. 안타깝습니다. ㅠ.ㅠ.')
            if self.human_count >=3:
                    print('\n\n 축하드립니다!! 봇을 이기셨습니다!! :)')


game=Game()
game.start()
