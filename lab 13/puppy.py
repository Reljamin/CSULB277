import state_asleep

class Puppy:
    def __init__(self):
        self._state = state_asleep.sleep()
        self._play = 0
        self._feed = 0

    def change_state(self, new_state):

        self._state = new_state

    def throw_ball(self):

        self._state.play()
        
    def give_food(self):

        self._state.feed()

    def inc_feeds(self):
        self._feed += 1

    def inc_plays(self):
        self._play += 1

    def reset(self):
        self._play = 0
        self._feed = 0

        