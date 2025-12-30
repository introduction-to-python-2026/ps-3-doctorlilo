def approximate_pi(n_terms):
    total_term = 0
    for i in range(n_terms):
       num = (-1) ** i / (2 * i + 1)
       total_term += num
    return 4 * total_term
