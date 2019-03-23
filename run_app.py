from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-576741841521-586892495062-583054601312-59ad90388a803b1b81b92f1bb62151f0', #app verification token
							'xoxb-576741841521-585464926018-Z55ehXRRNmBd8FVrUrFTex1Z', # bot verification token
							't33oKs9y15YjYjYxY6EG4Xwt', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))