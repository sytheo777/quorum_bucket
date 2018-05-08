#class ClassifiedBuckets():
#	QuorumSubspace qss =
#		"Users[DashCore]"
#		"Proposals[DashCoreMain]"
#		""

from ba_ma import BaseConverter

base58 = BaseConverter(
  'ABCDEFGHJKLMNPQRSTUVWXYZ123456789abcdefghijkmnopqrstuvwxyz'
  # Base57 is essentially Base62, but with five characters removed 
  # (I, O, l, 1, 0) because they are often mistaken for one another.
)

class QuorumPath():
	floor = 0
	def setup(self):
		self.floor = base58.to_decimal("AAAAA")

	def pad_element(self, el):
		while len(el) < 5:
			el += "A"

		return el

	def cast_path(self, fi, se):
		if self.floor == 0: self.setup()

		fi = self.pad_element(fi)
		se = self.pad_element(se)

		i = base58.to_decimal(fi)
		return i - self.floor


class QuorumBucket():
	def ParsePair(self, pair_str):
		import re
		# parse parse for [], split out into two groups
		m = re.search('([a-zA-Z]+)\[([a-zA-Z]+)\]', pair_str)
		# m.group(0) #- full string
		main = m.group(1)
		second = m.group(2)

		return main, second

	def AddLocationPair(self, location_str):
		fi, se = self.ParsePair(location_str)
		#self.get_network_positions(fi, se)
		print location_str

qp = QuorumPath()
print qp.pad_element("A")
print qp.cast_path("Users", "B")

#qub = QuorumBucket()
#print qub.AddLocationPair("Users[DashCore]")
#print 