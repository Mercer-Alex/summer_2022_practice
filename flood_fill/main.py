def flood_fill(image, sr, sc, color):
    rows = len(image)
    cols = len(image[0])
    curr_pixel = image[sr][sc]

    def flood(row, col):
        if row < 0 or col < 0 or row > rows-1 or col > cols-1 or image[row][col] == color or image[row][col] != curr_pixel:
            return
        image[row][col] = color
        flood(row+1, col)
        flood(row-1, col)
        flood(row, col+1)
        flood(row, col-1)

    flood(sr, sc)
    return image


input_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

print(flood_fill(input_image, sr, sc, newColor))

