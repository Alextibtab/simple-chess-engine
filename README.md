# Simple Chess Engine

```
                                                     _:_
                                                    '-.-'
                                           ()      __.'.__
                                        .-:--:-.  |_______|
                                 ()      \____/    \=====/
                                 /\      {====}     )___(
                      (\=,      //\\      )__(     /_____\
      __    |'-'-'|  //  .\    (    )    /____\     |   |
     /  \   |_____| (( \_  \    )__(      |  |      |   |
     \__/    |===|   ))  `\_)  /____\     |  |      |   |
    /____\   |   |  (/     \    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\    /____\    /_____\
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
   (______)(_______)(_______)(________)(________)(_________)
```

Welcome to My Chess Engine! This is a project where I develop a chess engine in Python, along with a graphical user interface (GUI) using the Kivy framework.

## Features

- Chess engine with move generation, move validation, and search algorithms.
- Graphical user interface (GUI) to interact with the chess engine.
- UCI (Universal Chess Interface) protocol support for communication between the GUI and the chess engine.
- Rendering of the chessboard, highlighting legal moves, and capturing user input.

## Requirements

- Python 3.x
- Libraries and frameworks:
    - python-chess
    - Stockfish
    - Pygame
    - numpy
    - pytest
    - kivy

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/my-chess-engine.git
    ```

2. Navigate to the project directory:

    ```shell
    cd my-chess-engine
    ```

3. Create a new virtual environment:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Linux/Mac:

      ```shell
      source venv/bin/activate
      ```

    - For Windows:

      ```shell
      venv\Scripts\activate
      ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Run the main application:

    ```shell
    python main.py
    ```

7. The GUI will be launched, allowing you to interact with the chess engine through the chessboard representation.

## Contributing

Contributions to My Chess Engine are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue or submit a pull request.

## Credits

- [python-chess](https://github.com/niklasf/python-chess) - Library for chess functionality.
- [Stockfish](https://stockfishchess.org/) - Open-source chess engine.
- [Pygame](https://www.pygame.org/) - Library for game development.
- [numpy](https://numpy.org/) - Library for efficient array operations.
- [pytest](https://pytest.org/) - Testing framework for Python.
- [Kivy](https://kivy.org/) - Framework for developing multi-touch applications.
- [ascii-art](https://www.asciiart.eu/sports-and-outdoors/chess) - Ascii Art created by Joan G. Stark.

## License

This project is licensed under the [MIT License](LICENSE).
