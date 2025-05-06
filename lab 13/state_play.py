import state_asleep
import puppy_state

class StatePlay(puppy_state.PuppyState):

    def play(self, puppy):
        

        puppy.inc_plays()

        if puppy.get_plays() == 1:
            return "The puppy wakes up and comes running to eat."
        elif puppy.get_plays() < 3:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy at so much it fell asleep!"




    def feed(self, puppy):


        return "noooooooooooooooooo i will ignore your food"


