from src.data import Case, Matter


def spread_row_col(c: Case, m_row: int, m_col: int) -> Case:
    new_case: Case = c.copy()
    new_case.matter_list = []
    m: Matter = c.matter_list[0]
    for i in range(m_row):
        for j in range(m_col):
            x0 = i * m.shape[0]
            y0 = j * m.shape[1]
            new_case.matter_list.append(Matter(m.values, x0, y0, m.background_color))
    new_case.shape = m.shape[0] * m_row, m.shape[1] * m_col
    return new_case
