# from ctypes import sizeof

def simplify(clauses, var, val) :
    res = []
    if val:
        lit = var
        neg = '~' + var
    else :
        lit = '~' + var
        neg = lit
    
    for clause in clauses:
        if lit in clause:
            continue
        tmp = clause.copy()
        if neg in tmp:
            tmp.remove(neg)
        if len(tmp) == 0 :
            return None
        res.append(tmp)

    return res


def dpll(clauses, assignment=None):
    """
    clauses: list of sets (e.g. {{'P', '~Q'}, {'Q'}})
    assignment: dict mapping variable -> bool
    Returns: (sat: bool, assignment)
    """
    """
    ref: https://en.wikipedia.org/wiki/DPLL_algorithm#The_algorithm
    """
    if assignment is None:
        assignment = {}
    ####### unit prop
    for clause in clauses:
        if len(clause) == 1:
            literal = next(iter(clause))
            if literal.startswith('~'):
                var = literal[1:]
                val = False
                # assignment[literal[1:]] = False
            else :
                var = literal
                val = True
                # assignment[literal] = True
            if var in assignment and assignment[var] != val :
                return False, assignment

            assignment[var] = val
            clauses = simplify(clauses, var, val)
            if clauses is None:
                return False, assignment
            
    ##### pure lit elimination\
    lits = set(l for c in clauses for l in c) 
    for l in lits:
        if l.startswith('~'):
            var = l[1:]
        else:
            var = l
        if var in assignment:
            continue
        if l.startswith('~'):
            if var not in lits:
                assignment[var] = False
        else :
            neg = '~' + var
            if neg not in lits :
                assignment[var] = True
        
        if var in assignment:
            clauses = simplify(clauses, var, assignment[var])
            if clauses is None:
                return False, assignment
        
    if not clauses :
        return True, assignment
    
    for clause in clauses :
        for literal in clause:
            if literal.startswith('~'):
                var = literal[1:]
            else:
                var = literal
            if var not in assignment:
                for val in (True, False) :
                    tmp = assignment.copy()
                    tmp[var] = val
                    tmp_cl = simplify(clauses, var, val)

                    if tmp is not None:
                        SAT, asgnmnt = dpll(tmp_cl, tmp)
                        if SAT:
                            return True, asgnmnt
                
                return False, assignment
            
    return False, assignment