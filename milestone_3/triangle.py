def get_triangle(rows: int) -> list[list[int]]:
    triangle = [[1]]
    for i in range(1, rows):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)    
    return triangle


def resulting_triangle(triangle: list[list[int]]):
    max_width = len(' '.join(str(e) for e in triangle[-1]))
    for row in triangle:
        padding = ' ' * ((max_width - len(' '.join(str(e) for e in row))) // 2)
        print(padding + ' '.join(str(e) for e in row))


if __name__ == "__main__":
    rows = (int(input("Enter the number of rows: ")))
    triangle = get_triangle(rows)
    resulting_triangle(triangle)

dir(rows)