def transition(nucleotid1, nucleotid2):
    """
    >>> transition('G', 'A')
    True
    >>> transition('t', 'g')
    False
    >>> transition('C', 'c')
    False
    """
    nucleotid1 = nucleotid1.upper()
    nucleotid2 = nucleotid2.upper()

    if (nucleotid1 == "A" and nucleotid2 == "G") or\
        (nucleotid1 == "G" and nucleotid2 == "A") or\
        (nucleotid1 == "C" and nucleotid2 == "T") or\
        (nucleotid1 == "T" and nucleotid2 == "C"):
        return True
    elif nucleotid1 == nucleotid2:
        return False
    else:
        return False

def transversion(nucleotid1, nucleotid2):
    """
    >>> transversion('G', 'A')
    False
    >>> transversion('t', 'g')
    True
    >>> transversion('C', 'c')
    False
    """

    if transition(nucleotid1, nucleotid2):
        return False
    elif nucleotid1.upper() == nucleotid2.upper():
        return False
    else:
        return True

def ratio(seq1, seq2):
    """
    >>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
    0.2222222222222222
    """
    c_transition = 0
    c_tranversion = 0
    ratio_numbers = 0
    for i in range(len(seq1)):
        if transition(seq1[i], seq2[i]) == True:
            c_transition += 1
        elif transversion(seq1[i], seq2[i]) == True:
            c_tranversion += 1

    if c_tranversion == 0:
        return 0.00
    else:
        ratio_numbers = c_transition / c_tranversion
        return ratio_numbers


if __name__ == '__main__':
    import doctest

    doctest.testmod()