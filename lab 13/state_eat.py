import puppy_state
import state_play
import state_asleep

class StateEat(puppy_state.PuppyState):


    def play(self, puppy):
        

        puppy.inc_plays()

        return "The puppy looks up from its food and chases the ball you threw."


    def feed(self, puppy):

        puppy.inc_feeds()

        if puppy.get_feeds() == 1:
            return "The puppy wakes up and comes running to eat."
        elif puppy.get_feeds() < 3:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy continues to eat as you add another scoop of kibble to its bowl. The puppy at so much it fell asleep!"

