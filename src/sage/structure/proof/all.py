def arithmetic(t = None):
    """
    Controls the default proof strategy for integer arithmetic algorithms (such as primality testing).

    INPUT:
    t -- boolean or None

    OUTPUT:
    If t == True, requires integer arithmetic operations to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
    If t == False, allows integer arithmetic operations to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
    If t is None, returns the integer arithmetic proof status.

    EXAMPLES:
    sage: proof.arithmetic()
    True
    sage: proof.arithmetic(False)
    sage: proof.arithmetic()
    False
    sage: proof.arithmetic(True)
    sage: proof.arithmetic()
    True
    """
    from proof import _proof_prefs
    return _proof_prefs.arithmetic(t)

def elliptic_curve(t = None):
    """
    Controls the default proof strategy for elliptic curve algorithms.

    INPUT:
    t -- boolean or None

    OUTPUT:
    If t == True, requires elliptic curve algorithms to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
    If t == False, allows elliptic curve algorithms to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
    If t is None, returns the current elliptic curve proof status.

    EXAMPLES:
    sage: proof.elliptic_curve()
    True
    sage: proof.elliptic_curve(False)
    sage: proof.elliptic_curve()
    False
    sage: proof.elliptic_curve(True)
    sage: proof.elliptic_curve()
    True
    """
    from proof import _proof_prefs
    return _proof_prefs.elliptic_curve(t)

def linear_algebra(t = None):
    """
    Controls the default proof strategy for linear algebra algorithms.

    INPUT:
    t -- boolean or None

    OUTPUT:
    If t == True, requires linear algebra algorithms to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
    If t == False, allows linear algebra algorithms to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
    If t is None, returns the current linear algebra proof status.

    EXAMPLES:
    sage: proof.linear_algebra()
    True
    sage: proof.linear_algebra(False)
    sage: proof.linear_algebra()
    False
    sage: proof.linear_algebra(True)
    sage: proof.linear_algebra()
    True
    """
    from proof import _proof_prefs
    return _proof_prefs.linear_algebra(t)

def number_field(t = None):
    """
    Controls the default proof strategy for number field algorithms.

    INPUT:
    t -- boolean or None

    OUTPUT:
    If t == True, requires number field algorithms to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
    If t == False, allows number field algorithms to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
    If t is None, returns the current number field proof status.

    EXAMPLES:
    sage: proof.number_field()
    True
    sage: proof.number_field(False)
    sage: proof.number_field()
    False
    sage: proof.number_field(True)
    sage: proof.number_field()
    True
    """
    from proof import _proof_prefs
    return _proof_prefs.number_field(t)

def polynomial(t = None):
    """
    Controls the default proof strategy for polynomial algorithms.

    INPUT:
        t -- boolean or None

    OUTPUT:
        If t == True, requires polynomial algorithms to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
        If t == False, allows polynomial algorithms to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
        If t is None, returns the current polynomial proof status.

    EXAMPLES:
        sage: proof.polynomial()
        True
        sage: proof.polynomial(False)
        sage: proof.polynomial()
        False
        sage: proof.polynomial(True)
        sage: proof.polynomial()
        True
    """
    from proof import _proof_prefs
    return _proof_prefs.polynomial(t)

def all(t = None):
    """
    Controls the default proof strategy throughout Sage.

    INPUT:
    t -- boolean or None

    OUTPUT:
    If t == True, requires Sage algorithms to (by default) return results that are true unconditionally: the correctness will not depend on an algorithm with a nonzero probability of returning an incorrect answer or on the truth of any unproven conjectures.
    If t == False, allows Sage algorithms to (by default) return results that may depend on unproven conjectures or on probabilistic algorithms.  Such algorithms often have a substantial speed improvement over those requiring proof.
    If t is None, returns the current global Sage proof status.

    EXAMPLES:
    sage: proof.all()
    {'polynomial': True, 'other': True, 'elliptic_curve': True, 'number_field': True, 'linear_algebra': True, 'arithmetic': True}
    sage: proof.number_field(False)
    sage: proof.number_field()
    False
    sage: proof.all()
    {'polynomial': True, 'other': True, 'elliptic_curve': True, 'number_field': False, 'linear_algebra': True, 'arithmetic': True}
    sage: proof.number_field(True)
    sage: proof.number_field()
    True
    """
    from proof import _proof_prefs
    if t is None:
        return _proof_prefs._require_proof.copy()
    for s in _proof_prefs._require_proof.iterkeys():
        _proof_prefs._require_proof[s] = bool(t)

from proof import WithProof