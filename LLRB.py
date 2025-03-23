class LLRBNode:
    def __init__(self, key, color, left=None, right=None):
        self.key = key
        self.color = color  # True indicates red, False indicates black
        self.left = left
        self.right = right
def is_red(node):
    return node is not None and node.color

def is_red(node):
    return node is not None and node.color

class LLRBTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = True
        return x

    def _rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = True
        return x

    def _flip_colors(self, h):
        h.color = not h.color
        if h.left:
            h.left.color = not h.left.color
        if h.right:
            h.right.color = not h.right.color

    def _insert(self, h, key):
        if h is None:
            return LLRBNode(key, True)
        if key == h.key:
            return h  # Ignore duplicates
        if key < h.key:
            h.left = self._insert(h.left, key)
        elif key > h.key:
            h.right = self._insert(h.right, key)
        if is_red(h.right) and not is_red(h.left):
            h = self._rotate_left(h)
        if is_red(h.left) and is_red(h.left.left):
            h = self._rotate_right(h)
        if is_red(h.left) and is_red(h.right):
            self._flip_colors(h)
        return h

    def insertElement(self, key):
        self.root = self._insert(self.root, key)
        self.root.color = False

    def searchElement(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False
    
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))