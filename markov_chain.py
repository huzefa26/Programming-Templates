from numpy import matmul, array, float
from numpy.linalg import inv, pinv

transition_probability_matrix = [
    [0, 2, 1, 1, 0], 
    [1, 1, 0, 2, 1],
    [0, 3, 2, 0, 0], 
    [0, 0, 0, 0, 0], 
    [2, 0, 1, 3, 0]
]
# [
#     [0, 1, 0, 0, 0, 1],
#     [4, 0, 0, 3, 2, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]

# [
#     [0, 2, 1, 0, 0],
#     [0, 0, 0, 3, 4],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]
transition_probability_matrix = array(transition_probability_matrix, float)


def transition_prob_matrix(mat):
    pass


def transfer_to_markov_chain(transition_probab_mat):
    for i in range(len(transition_probab_mat)):
        x = sum(transition_probab_mat[i])
        if x:
            for j in range(len(transition_probab_mat)): transition_probab_mat[i][j] /= x
        else:
            transition_probab_mat[i][i] = 1


def get_stationary_matrix(mat):
    # [a, b] . [[.1, .9], [.3, .7]]  = [a, b]
    #
    # .1 a + .3 b  = a
    # .9 a + .7 b  = b
    #
    # a + b = 1
    #
    # .1 a + .3 (1-b) = a
    # .3 (1-b) = .9 a
    # 1 - b = 3 a
    # 3a + b = 1
    #
    # a = 0
    # b = 1
    #
    pass


print('A:')
for x in transition_probability_matrix:
    print(x)

absorbing_states = [i for i in range(len(transition_probability_matrix)) if not sum(transition_probability_matrix[i])]

transfer_to_markov_chain(transition_probability_matrix)
print('\nA Markov Chain:')
for x in transition_probability_matrix:
    print(x)


def to_standard_form(abs_mat, absorbing_states):
    non_abs_states = [i for i in range(len(abs_mat)) if i not in absorbing_states]
    standard_mat = array([[0] * len(abs_mat) for _ in range(len(abs_mat))], dtype=float)
    R = [[None] * len(absorbing_states) for _ in range(len(non_abs_states))]
    Q = [[None] * len(non_abs_states) for _ in range(len(non_abs_states))]
    for i in range(len(absorbing_states)):
        standard_mat[i][i] = 1
    for i in range(len(non_abs_states)):
        for j in range(len(absorbing_states)):
            standard_mat[i + len(absorbing_states)][j] = abs_mat[non_abs_states[i]][absorbing_states[j]]
            R[i][j] = abs_mat[non_abs_states[i]][absorbing_states[j]]
        for j in range(len(non_abs_states)):
            standard_mat[i + len(absorbing_states)][j + len(absorbing_states)] = abs_mat[non_abs_states[i]][
                non_abs_states[j]]
            Q[i][j] = abs_mat[non_abs_states[i]][non_abs_states[j]]
    return standard_mat, R, Q


standard_absorbing_matrix, R, Q = to_standard_form(transition_probability_matrix, absorbing_states)

print('\nStandard Absorbing Matrix:')
for x in standard_absorbing_matrix:
    print(x)
print(R)
# print(Q)

# transfer_to_markov_chain(standard_absorbing_matrix)
# print(standard_absorbing_matrix)

#
# standard form, P = [[I 0][R Q]]
# limiting matrix Pbar = [[I 0] [FR 0]]
# fundamental matrix for P, F = (I-Q)^-1
#


def get_fundamental_matrix(Q):
    F = Q.copy()
    # print(F)
    for i in range(len(F)):
        F[i][i] -= 1
        for j in range(len(F)): F[i][j] *= -1
    # print('\nI-Q:')
    # for i in F:
    #     print(i)
    try:
        return inv(F)
    except:
        return pinv(F)


def get_limiting_matrix_for_absorbing_markov_chain(P, Q, R):
    F = get_fundamental_matrix(array(Q))
    print('\nF:')
    for i in F:
        print(i)
    F = matmul(F, R)
    print('\nFR:')
    for i in F:
        print(i)
    lenI = len(P) - len(R)
    Pbar = P.copy()
    for i in range(len(R)):
        for j in range(len(R[0])):
            Pbar[i + lenI][j] = F[i][j]
        for j in range(len(Q[0])):
            Pbar[i + lenI][j + len(R[0])] = 0
    return Pbar


# transfer_to_markov_chain(standard_absorbing_matrix)
# print(standard_absorbing_matrix)
limiting_matrix = get_limiting_matrix_for_absorbing_markov_chain(standard_absorbing_matrix, Q, R)
print('\nLimiting matrix:')
for i in limiting_matrix:
    print(i)


def transfer_to_markov_chain(transition_probab_mat):
    for i in range(len(transition_probab_mat)):
        x = sum(transition_probab_mat[i])
        if x:
            for j in range(len(transition_probab_mat)): transition_probab_mat[i][j] /= x
        else:
            transition_probab_mat[i][i] = 1


def get_fundamental_matrix(Q):
    F = Q.copy()
    for i in range(len(F)):
        F[i][i] -= 1
        for j in range(len(F)):
            F[i][j] *= -1
    try:
        return inv(F)
    except:
        return pinv(F)


def test(m):
    m = array(m, float)
    absorbing_states = [i for i in range(len(m)) if not sum(m[i])]
    if len(absorbing_states) == len(m):
        return [1] + [0]*(len(m)-1) + [1]
    transfer_to_markov_chain(m)
    non_abs_states = [i for i in range(len(m)) if i not in absorbing_states]
    R = [[None] * len(absorbing_states) for _ in range(len(non_abs_states))]
    Q = [[None] * len(non_abs_states) for _ in range(len(non_abs_states))]
    for i in range(len(non_abs_states)):
        for j in range(len(absorbing_states)):
            R[i][j] = m[non_abs_states[i]][absorbing_states[j]]
        for j in range(len(non_abs_states)):
            Q[i][j] = m[non_abs_states[i]][non_abs_states[j]]
    F = get_fundamental_matrix(array(Q))
    # print(F)
    F = matmul(F, R)
    F = F[0]
    # getting proper fractions from the results as the values are float and below code gives the proper numerators and denominator
    # if you need float values, then just add 'return F' and delete the below for loop 
    for i in range(1, 101):
        poss = True
        temp = [round(f * i, 6) for f in F]
        for t in temp:
            if t != int(t):
                poss = False
                break
        if poss:
            return [int(t) for t in temp], [int(sum(temp))]  # list of numerators, common denominator


# test([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# test([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# test([[0, 2, 1, 1, 0], [1, 1, 0, 2, 1], [0, 3, 2, 0, 0], [0, 0, 0, 0, 0], [2, 0, 1, 3, 0]])

test([
    [2, 1, 2],
    [0, 1, 0],
    [0, 0, 0],
])
