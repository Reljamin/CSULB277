import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):

    def play(self, puppy):
        return "NO"

    def feed(self, puppy):
        puppy.change_state(state_eat.StateEat())
        puppy.inc_feed()
        return f"pupper ate: {get_feed()}"ß