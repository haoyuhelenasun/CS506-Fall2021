from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path) as read_file:
        csv_file = reader(read_file)
        matrix = []
        for row in csv_file:
            r = []
            for col in row:
                if col.isnumeric():
                    col = int(col)
                r.append(col)
            matrix.append(r)
    return matrix
