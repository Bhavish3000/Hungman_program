""""_ASCII images for the main module
"""
stages = [  # final state: head, torso, both arms, and both legs
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        # head, torso, both arms, no legs
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        # head, torso, one arm, no legs
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        # head and torso only
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        # head only
        """
           -----
           |   |
           |   
           |
           |
           -
        """,
        # initial empty state
        """
           -----
           |   |
           |
           |
           |
           -
        """,
    ]