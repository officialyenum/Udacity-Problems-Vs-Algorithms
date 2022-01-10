# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root="Not Found"):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root)

    def insert(self, routes, handler):
        # Similar to our previous example you will want to recursively add nodes
        # ---- Recursion Method ----
        current_node = self.root
        node = self.insertRec(current_node, routes, 0)
        node.handler = handler
        # print('Handler Name Again : {}'.format(node.handler))
        # ---- Traverse Method -----
        # for route in routes:
        #     if route not in current_node.children:
        #         current_node.children[route] = RouteTrieNode()
        #     current_node = current_node.children[route]
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        #Insert handler tp current node
        # current_node.handler = handler
    
    def insertRec(self, node, routes, index):
        # Base recursion
        if len(routes) <= index:
            return node
        
        if routes[index] not in node.children:
            node.children[routes[index]] = RouteTrieNode()  
        #     print('Handler Name Again : {}'.format(node.handler))
        # print('Routes Name : {}'.format(routes[index]))
        node = node.children[routes[index]]
        node = self.insertRec(node, routes, index + 1)
        return node


    def find(self, routes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None/Not Found for no match
        if len(routes) == 0:
            return self.root.handler

        current_node = self.root
        for route in routes:
            if route not in current_node.children:
                return "Not Found"
            current_node = current_node.children[route]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler="Not Found"):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, route, handler):
        # Insert the node as before
        self.children[route] = RouteTrieNode(handler)
    
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler="root handler"):
        # Create a new RouteTrie for holding our routes
        self.route_trie = RouteTrie(handler)
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie.root.handler = handler

    def add_handler(self, route, handler): # Add a handler for a path
        if route == "" or handler == "":
            # route and handler cannot be empty do nothing
            return
        # You will need to split the path and
        routes = self.split_path(route)
        #  pass the pass parts as a list to the RouteTrie
        self.route_trie.insert(routes , handler)
        pass

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        routes = self.split_path(route)
        return  self.route_trie.find(routes)

    def split_path(self, route):
        if route == "/":
            return []
        # you need to split the path into parts for 
        routes = route.split('/')
        for ele in routes:
            if ele == '':
                routes.remove(ele)
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return routes

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
# Test Case 1
print('-----Test Case 1-----')
print(router.lookup("/")) # should print 'root handler'

print(router.lookup("")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/", "about handler")  # add a route


# Test Case 2
print('-----Test Case 2-----')
router2 = Router("root handler") 
router2.add_handler("/admin/users", "users handler")
router2.add_handler("/admin/users/84", "user 84 handler")
router2.add_handler("/admin/dashboard/", "dashboard handler")

print(router2.lookup("/"))# should print 'root handler'
print(router2.lookup("/admin/users/84")) # should print 'user 84 handler'
print(router2.lookup("/admin/users/")) # should print 'usershandler' or Not Found if you did not handle trailing slashes
print(router2.lookup("/admin/dash/")) # should print 'not found handler' or None if you did not implement one

# Test Case 3
print('-----Test Case 3-----')
router3 = Router() 
router3.add_handler("/profile", "profile handler")
print(router3.lookup("/profile")) # should print 'profile handler'
router3.add_handler("/84", "user 84 handler")
router3.add_handler("", "dashboard handler") # dashboard handler will not be created 
router3.add_handler("/profile", "") # profile route will not be created because it has no handler
router3.add_handler("/profile", "New profile handler") # profile route will over ride previous handler

print(router3.lookup("/"))# should print 'root handler'
print(router3.lookup("/profile")) # should print 'New profile handler'
print(router3.lookup("/admin/users/")) # should print 'usershandler' or Not Found if you did not handle trailing slashes
print(router3.lookup("/admin/dash/")) # should print 'not found handler' or None if you did not implement one