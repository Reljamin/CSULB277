import state_asleep

class Puppy:
    def __init__(self):
        self._state = state_asleep.StateAsleep()
        self._plays = 0
        self._feeds = 0

    def change_state(self, new_state):

        self._state = new_state

    def throw_ball(self):

        self._state.play()
        
    def give_food(self):

        self._state.feed()
    
    def inc_feeds(self):
        self._feeds += 1

    def inc_plays(self):
        self._plays += 1


    def get_plays(self):
        return self._play

    def get_feeds(self):
        return self._feed

    def reset(self):
        self._plays = 0
        self._feeds = 0

        