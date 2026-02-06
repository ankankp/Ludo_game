# board/path.py

# Border movement path (15x15 grid based)

PATH = [

    # Top row (left → right)
    (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),

    # Turn down
    (5,6),(4,6),(3,6),(2,6),(1,6),(0,6),

    # Top center → right
    (0,7),(0,8),

    # Down right side
    (1,8),(2,8),(3,8),(4,8),(5,8),

    # Enter right row
    (6,9),(6,10),(6,11),(6,12),(6,13),(6,14),

    # Down
    (7,14),(8,14),

    # Bottom right → left
    (8,13),(8,12),(8,11),(8,10),(8,9),

    # Down to bottom
    (9,8),(10,8),(11,8),(12,8),(13,8),(14,8),

    # Bottom center → left
    (14,7),(14,6),

    # Up left side
    (13,6),(12,6),(11,6),(10,6),(9,6),

    # Enter left row
    (8,5),(8,4),(8,3),(8,2),(8,1),(8,0),

    # Up
    (7,0)
]
