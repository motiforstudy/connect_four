



def create_board(cols: int = 7, rows: int = 6) -> list[list[str]]:

    return [[""]]


def column_is_full(board: list[list[str]], col: int) -> bool:

    return True


def drop_disc(board: list[list[str]], col: int, mark: str) -> tuple[int,int] | None:

    return None


def legal_moves(board: list[list[str]]) -> list[int]:

    return [1]


def render(board: list[list[str]], one_based_cols: bool = True) -> str:

    return ""