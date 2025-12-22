class Expr:
    pass 

class Var(Expr):
    def __init__(self, name):
        self.name = name
        self.type = "var"
    
class Not(Expr):
    def __init__(self, expr):
        self.expr = expr
        self.type = "not"

class And(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "and"

class Or(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "or"
class Implies(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "implies"

def del_implies(expr):
    if expr.type == "var":
        return expr
    elif expr.type == "not":
        return Not(del_implies(expr.expr))
    elif expr.type == "and":
        return And(del_implies(expr.left), del_implies(expr.right))
    elif expr.type == "or":
        return Or(del_implies(expr.left), del_implies(expr.right))
    elif expr.type == "implies":
        return Or(Not(del_implies(expr.left)), del_implies(expr.right))


def push_not(expr):
    if expr.type == "var":
        return expr
    elif expr.type == "not":
        if expr.expr.type == "var":
            return expr
        elif expr.expr.type == "not":
            return push_not(expr.expr.expr)
        elif expr.expr.type == "and":
            return Or(push_not(Not(expr.expr.left)), push_not(Not(expr.expr.right)))
        elif expr.expr.type == "or":
            return And(push_not(Not(expr.expr.left)), push_not(Not(expr.expr.right)))
    elif expr.type == "and":
        return And(push_not(expr.left), push_not(expr.right))
    elif expr.type == "or":
        return Or(push_not(expr.left), push_not(expr.right))
    

def distri(expr):
    if expr.type == "var":
        return [{expr.name}]
    elif expr.type == "not":
        return [{"~" + expr.expr.name}]
    elif expr.type == "and":
        return distri(expr.left) + distri(expr.right)
    elif expr.type == "or":
        left = distri(expr.left)
        right = distri(expr.right)

        res = []
        for l in left:
            for r in right:
                res.append(l | r)
        return res
        

def to_cnf(expr):
    """
    Converts a propositional logic expression to CNF.
    Returns a list of clauses, each clause is a set of literals.
    """
    expr = del_implies(expr)
    expr = push_not(expr)
    return distri(expr)
   # distr or over ands