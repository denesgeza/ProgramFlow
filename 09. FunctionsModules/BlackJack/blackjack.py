import random
import tkinter as t


def load_images(card_images):
    suits = ['heart', 'diamond', 'club', 'spade']
    face_cards = ['jack', 'queen', 'king']
    extension = 'ppm'

    # for each suit retrieve the image for the cards
    for suit in suits:
        # first tje number cards 1 to 10
        for card in range(1, 10):
            name = f'cards/{str(card)}_{suit}.{extension}'
            image = t.PhotoImage(file=name)
            card_images.append((card, image))
        # the face cards
        for card in face_cards:
            name = f'cards/{str(card)}_{suit}.{extension}'
            image = t.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off the deck
    next_card = deck.pop(0)
    # and add it to the back of the pack
    deck.append(next_card)
    # add the image to a Label and display the Label
    t.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # only one ace can have the value of 11 and this will be reduced
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if more than 21, check ace and subtract
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set('Dealer wins!')
    if dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player wins!')
    elif dealer_score > player_score:
        result_text.set('Dealer wins!')
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = t.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold the players card images
    player_card_frame = t.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set('')
    # create a list to store the hands
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = t.Tk()

# setup screen for dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

result_text = t.StringVar()
result = t.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = t.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = t.IntVar()
t.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
t.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = t.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = t.IntVar()

t.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
t.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = t.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = t.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = t.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = t.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = t.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = t.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
# log cards
cards = []
load_images(cards)
# create a list of cards and shuffle them
# deck is a new list, to avoid remaining without cards
# add more packs to the deck
deck = list(cards) + list(cards) + list(cards)
shuffle()

# create a list to store the hands
dealer_hand = []
player_hand = []

if __name__ == '__main__':
    play()