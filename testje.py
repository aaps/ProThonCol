from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import json
import datetime


class Message:
	cargolength = 0
	cargo = ""

	def __init__(self, cargo):
		self.cargo = cargo
		self.timestamp = datetime.datetime.utcnow()
		self.cargolength = len(cargo)



class Actor:
	
	uid = ""
	listento = []
	listen = False
	send = False
	actortype = ""
	messages = []
	connected = True

	def __init__():
		pass


class Chat(LineReceiver):

	def __init__(self, actors):
		self.actors = actors
		self.name = None
		self.state = "GETNAME"
		self.delimiter = "\n"
		msgexpire = None

	def connectionMade(self):
		protocol.sendLine("connected")

	def connectionLost(self, reason):
		if self.name in self.actors:
			del self.actors[self.name]

	# de naam moet staan in een lijn json, ofwel uid, handle getname moet weg.
	def lineReceived(self, line):
		line = json.decode(line)
		uid = line["uid"]
		if uid in self.actors:
			# self.actors[uid].messages.append(line["message"])
			self.actors[uid].tags = line["tags"]
		else:
			actor = Actor()
			actor.uid = line["uid"]
			actor.listen = line["listen"]
			actor.send = send["listen"]
			actor.actortype = send["actortype"]
			actor.tags = line["tags"]
			mesage = Mesage()
			mesage.cargo = send["cargo"]
			actor.messages.append(mesage)
			
			self.actors.append(actor)

			


class ChatFactory(Factory):

	def __init__(self):
		self.actors = {} # maps user names to Chat instances

	def buildProtocol(self, addr):
		return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()


# json actor
	# uid
	# listento
	# listen
	# send
	# type
	# hash
	# cargolength


# connection class
	# linereceved
	# registerlistner
	# redirectmessages
	# savemessages
	# sendmessages
	# showallregistered

# class actor
	# uid
	# listento
	# listen
	# send
	# type
	# messages

# class messages
	# cargolength
	# hash
	# cargo

