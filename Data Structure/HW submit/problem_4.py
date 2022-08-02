class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def dfs(set, user, group):
    if group in set:
        return False
    
    if user in group.get_users():
        return True
    
    set.add(group)
    for g in group.get_groups():
        
        if dfs(set, user, g):
            return True
    
    return False


def is_user_in_group(user, group):
    
    
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group == None or user == None :
        return False
    
    return dfs(set(), user, group)



# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def test_None():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, None))  # False



# Test Case 2
def test_defalt():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))  # True


# Test Case 3
def test_finite():
    a = Group("a")
    b = Group("b")
    c = Group("c")
    d = Group("d")
    e = Group("e")

    user = "user"
    e.add_user(user)

    d.add_group(e)
    c.add_group(d)
    b.add_group(c)
    a.add_group(b)
    d.add_group(a)
    c.add_group(b)

    print(is_user_in_group(user, a))  # True




test_None()
test_defalt()
test_finite()