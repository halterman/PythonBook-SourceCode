from dot import Dot
from turtle import Screen, Turtle


def main():
    # Make a Dot object
    d = Dot(screen=Screen(), turtle=Turtle(), x=10, y=20)
    # Run the graphical program
    d.run()


if __name__ == "__main__":
    main()
