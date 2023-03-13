from abc import ABC, abstractmethod
import pickle
import jsonpickle

class Persist(ABC):
	def __init__(self) -> None:
		pass

	@abstractmethod
	def save(self, menu):
		pass

	@abstractmethod
	def load(self):
		pass

class PersistBinary(Persist):
	def __init__(self) -> None:
		super().__init__()
		self._gagfile = './gag.bjson'

	def save(self, menu):
		with open(self._gagfile, mode='wb') as bin_file:
			pickle.dump(menu, bin_file)

	def load(self):
		with open(self._gagfile, mode='wb') as bin_file:
			menu = pickle.load(bin_file)
		return menu

class PersistJson(Persist):
	def __init__(self) -> None:
		super().__init__()
		self._gagfile = './gag.json'

	def save(self, menu):
		with open(self._gagfile, 'w') as json_file:
			menu_str = jsonpickle.encode(menu)
			json_file.write(menu_str)

	def load(self):
		menu = None
		with open(self._gagfile, 'r') as json_file:
			menu_str = json_file.read()
			try:
				menu = jsonpickle.decode(menu_str)
			except:
				print('Unable to load file')
		return menu