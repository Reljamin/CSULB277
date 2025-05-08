import state_asleep
import puppy_state

class StatePlay(puppy_state.PuppyState):

    def play(self, puppy):
        

        puppy.inc_plays()

        if puppy.get_plays() == 1:
            return "The puppy looks up from its food and chases the ball you threw."
        elif puppy.get_plays() < 3:
            return "You throw the ball again and the puppy excitedly chases it"
        else:
            puppy.change_state(state_asleep.StateAsleep())

            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it. The puppy played so much it fell asleep!"




    def feed(self, puppy):


        return "The puppy is too busy playing with the ball to eat right now"


