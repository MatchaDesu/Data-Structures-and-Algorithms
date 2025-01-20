class Song :
    def __init__(self, name:str, genre:str, durations:int) :
        self.name = name
        self.genre = genre
        self.durations = durations
    
    def show_info(self) :
        minutes, seconds = divmod(self.durations, 60)
        return (f"{self.name} <|> {self.genre} <|> {minutes}.{seconds:>02}")


Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())