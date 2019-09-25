

class LockingTreeNode:
	def __init__(self, val, left = None, right = None, parent = None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent 
		self._is_locked = False;
		self.locked_descendent_count = 0

	def _can_lock_or_unlock(self):
		if self.locked_descendent_count > 0:
			return False

		cur = self.parent
		while cur:
			if cur._is_locked == True:
				return False

			cur = cur.parent

		return True

	def is_locked(self):
		return self._is_locked

	def lock(self):
		if self._can_lock_or_unlock():
			self._is_locked = True

			cur = self.parent
			while cur:
				cur.locked_descendent_count += 1
				cur = cur.parent
			return True
		else:
			return False

	def unlock(self):
		if self._can_lock_or_unlock():
			self._is_locked = False

			cur = self.parent
			while cur:
				cur.locked_descendent_count -= 1
				cur = cur.parent
			return True
		else:
			return False






