import random

class ActionSpace(object):
	def __init__(self, actions):
		self.n = len(actions)
		self.actions = actions

	def sample(self):
		return random.randint(0, self.n-1)

	def name(self, action):
		return actions[name]

	def validate(self, action):
		return action is not None and action >= 0 and action < self.n

class Env(object):

	def __init__(self, num_agents, actions):
		self.num_agents = num_agents
		self.action_space = ActionSpace(actions)
		self.states = []
		self.observations = []

class Hats(Env):

	def __init__(self, num_agents, actions):
		super(Hats, self).__init__(num_agents, actions)
		self.reset()
		self.recompute_observations()

	def reset(self):
		self.last_actions = [None]*self.num_agents
		self.states = [random.randint(0,1) for agent in xrange(self.num_agents)]

	def recompute_observations(self):
		self.observations = [[self.last_actions[i] for i in xrange(agent)] +[self.states[j] for j in xrange(agent+1, self.num_agents)] for agent in xrange(self.num_agents)]

	def step(self, agent, action):
		if not self.action_space.validate(action):
			return None
		self.last_actions[agent] = action
		self.recompute_observations()
		done = None not in self.last_actions
		reward = 0 if not done else sum([act == state for (act, state) in zip(self.last_actions, self.states)])
		return (reward, done)

	def get_obs(self, agent):
		obs = self.observations[agent]
		if None in obs:
			return None
		return obs


class Switch(Env):
	def __init__():
		pass

def play_hats():
	#start
	print "Starting"
	env = Hats(3, [0, 1])
	print "States: %s"%env.states
	print "Actions so far: %s"%env.last_actions
	print "Available observations: %s"%env.observations

	print env.get_obs(2)

	#agent 0 turn
	print "############################################"
	print "Agent 0 turn"
	print "Observation: %s"%env.get_obs(0)
	print "(Reward: %s, GameOver: %s)"%env.step(0, 0)
	print "Actions so far: %s"%env.last_actions
	print "Available observations: %s"%env.observations

	#agent 1 turn
	print "############################################"
	print "Agent 1 turn"
	print "Observation: %s"%env.get_obs(1)
	print "(Reward: %s, GameOver: %s)"%env.step(1, 0)
	print "Actions so far: %s"%env.last_actions
	print "Available observations: %s"%env.observations

	#agent 2 turn
	print "############################################"
	print "Agent 2 turn"
	print "Observation: %s"%env.get_obs(2)
	print "(Reward: %s, GameOver: %s)"%env.step(2, 0)
	print "Actions so far: %s"%env.last_actions
	print "Available observations: %s"%env.observations

play_hats()

