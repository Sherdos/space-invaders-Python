class Stats:
    """Статистика игры"""
    
    
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        self.high_score = self.get_high_score()
        
    
    def reset_stats(self):
        '''Изменение статистика'''
        self.hp = 0
        self.score = 0
        
    def get_high_score(self):
        with open('./high_score.txt', 'r') as f:
            return int(f.readline())
    
    