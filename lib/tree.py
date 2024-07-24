class Tree:
    def __init__(self, root=None):
        '''Initialize the tree with a root node.'''
        self.root = root

    def get_element_by_id(self, id):
        '''Recursively search for an element by its ID.'''
        def search(node):
            if node is None:
                return None
            # Check if the current node has the matching id
            if node.get('id') == id:
                return node
            # Recursively search in the children
            for child in node.get('children', []):
                result = search(child)
                if result is not None:
                    return result
            return None
        
        return search(self.root)
