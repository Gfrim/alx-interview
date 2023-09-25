def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            # Calculate the middle elements based on the previous row
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j - 1] + triangle[-1][j])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle

# Example: Generate Pascal's Triangle with 5 rows

