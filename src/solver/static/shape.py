from src.data import Case, Problem


def is_constant(p: Problem) -> bool:

    cy0: Case = p.train_y_list[0]

    size_row: int = cy0.shape[0]
    size_col: int = cy0.shape[1]

    cy: Case

    for cy in p.train_y_list:
        if cy.shape[0] != size_row or cy.shape[1] != size_col:
            return False
    return True
