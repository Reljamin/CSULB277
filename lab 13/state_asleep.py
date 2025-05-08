import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):

    def play(self, puppy):

        return "The puppy is asleep. It doesn't want to play right now."

    def feed(self, puppy):

        puppy.inc_feeds()

        puppy.change_state(state_eat.StateEat())
        
        return "The puppy wakes up and comes running to eat."