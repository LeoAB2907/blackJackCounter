from pynput import keyboard

running_count = 0
true_count = 0
num_decks = 8
cards_played = 0
quit_loop = False


class KeyPressedException(Exception):
    pass


def adjust_count(num):
    global running_count, num_decks, cards_played, true_count
    running_count += num
    cards_played += 1
    if cards_played == 52:
        cards_played = 0
        num_decks -= 1
    true_count = running_count/num_decks


def shuffle():
    global running_count, num_decks, cards_played, true_count
    true_count = 0
    num_decks = 8
    cards_played = 0
    running_count = 0


def print_count():
    print("True count: %s; Running Count: %s; Decks Left: %s" % (round(true_count,1), running_count, num_decks))


def on_press(key):
    raise KeyPressedException(key.char)


def main():
    global quit_loop, num_decks

    while not quit_loop:
        with keyboard.Listener(on_press=on_press) as listener:
            try:
                listener.join()
            except KeyPressedException as e:
                key = e.args[0]
                if key == '+':
                    adjust_count(1)
                    print_count()
                elif key == '-':
                    adjust_count(-1)
                    print_count()
                elif key == '0':
                    adjust_count(0)
                    print_count()
                elif key == '4':
                    num_decks = 4
                    print("Decks set to 4")
                elif key == '6':
                    num_decks = 6
                    print("Decks set to 6")
                elif key == '8':
                    num_decks = 8
                    print("Decks set to 8")
                elif key == 's':
                    shuffle()
                    print("Shuffled")
                elif key == "q":
                    quit_loop = True
                pass


if __name__ == '__main__':
    main()

