import re
from rasa.nlu.components import Component

class Preprocessor(Component):
	name = "remove_punctuation"
	provides = [name]
	
	def init(self, component_config=None):
		super(Preprocessor, self).init(component_config)
	
	def process(self, message, **kwargs):
		phrase = message.text
		phrase = re.sub(r'[^a-zA-Z0-9]+', " ", phrase)
		
		# Trim leading or trailing spaces...
		phrase = phrase.strip()
		found = []
		entry = {"original": message.text,"cleansed": phrase}
		found.append(entry)
		message.set(self.name,message.get(self.name, []) + found,add_to_output=True)
		message.text=phrase