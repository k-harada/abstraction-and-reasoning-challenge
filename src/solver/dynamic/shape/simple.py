from src.data import Case, Problem


def is_same(p: Problem) -> bool:

    cx: Case
    cy: Case

    for cx, cy in zip(p.train_x_list, p.train_y_list):
        if cx.shape[0] != cy.shape[0] or cx.shape[1] != cy.shape[1]:
            return False
    return True


def is_multiple(p: Problem) -> bool:

    cx0: Case = p.train_x_list[0]
    cy0: Case = p.train_y_list[0]

    if cy0.shape[0] % cx0.shape[0] != 0 or cy0.shape[1] % cx0.shape[1] != 0:
        return False
    m_row: int = cy0.shape[0] // cx0.shape[0]
    m_col: int = cy0.shape[1] // cx0.shape[1]

    cx: Case
    cy: Case

    for cx, cy in zip(p.train_x_list, p.train_y_list):
        if cx.shape[0] * m_row != cy.shape[0] or cx.shape[1] * m_col != cy.shape[1]:
            return False
    return True


def is_constant(p: Problem) -> bool:

    cy0: Case = p.train_y_list[0]

    size_row: int = cy0.shape[0]
    size_col: int = cy0.shape[1]

    cy: Case

    for cy in p.train_y_list:
        if cy.shape[0] != size_row or cy.shape[1] != size_col:
            return False
    return True
