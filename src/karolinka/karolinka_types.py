class Tabela(list[list[str]]):
    """
    Dwuwymiarowa lista z tekstem w środku.

    Przykład:

    [
        ["A", "B" ,"C"], \n
        ["D", "E" ,"F"], \n
    ]

    """
    def __init__(self, value): 
        super().__init__(value)
