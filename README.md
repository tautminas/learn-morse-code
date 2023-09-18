# Learn Morse Code

## About the application
Learn Morse Code is a GUI application designed to help you learn Morse code efficiently. Learning the Morse code is not such a daunting task if the right memory techniques are used for learning it. It was perfectly shown by Nelson Dellis (memory athlete) in his [YouTube](https://www.youtube.com/watch?v=D8tPkb98Fkk) video. The application utilizes his learning approach.

## Running the program
Run the application:
```bash
python main.py
```

You can make an executable file for easier future reuse (it will be generated in the dist/ directory):
```bash
pyinstaller --onefile --noconsole --add-data "assets;assets" --icon="./assets/morse-code.ico" --name="learn-morse-code" main.py
```