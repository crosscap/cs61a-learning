"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    index = 0
    for word in paragraphs:
        if select(word) == True:
            if (index == k):
                return word
            else:
                index += 1
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2

    def compare_strList_with_topic(str_list):
        clean_str_list = lower(remove_punctuation(str_list))
        words = split(clean_str_list)
        for word in words:
            if word in topic:
                return True
        return False
    return compare_strList_with_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    index, same_counter = 0, 0
    str_length = min(len(typed_words), len(reference_words))
    if str_length == 0:
        return 0.0
    while index < str_length:
        if typed_words[index] == reference_words[index]:
            same_counter += 1
        index += 1
    return (same_counter / len(typed_words)) * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    min_diff = limit
    min_word = ''
    for vaild_word in valid_words:
        if user_word == vaild_word:
            return user_word
        diff_num = diff_function(user_word, vaild_word, limit)
        if (min_word == '' and diff_num <= min_diff) \
                or (min_word != '' and diff_num < min_diff):
            min_diff = diff_num
            min_word = vaild_word
        # print("DEBUG:", vaild_word, diff_num, min_word)

    return min_word if min_word != '' else user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # assert False, 'Remove this line'
    # BEGIN PROBLEM 6
    if start == '' or goal == '' or limit < 0:
        return abs(len(goal) - len(start))
    elif start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    else:
        return shifty_shifts(start[1:], goal[1:], limit - 1) + 1
    # END PROBLEM 6

    # Implemention with halper function
    # def halper(start, goal, limit, counter):
    #     chenge_count = abs(len(goal) - len(start))
    #     if start == '' or goal == '':
    #         return counter
    #     elif counter == limit + 1:
    #         return limit + 1
    #     elif start[0] == goal[0]:
    #         return halper(start[1:], goal[1:], limit, counter)
    #     else:
    #         return halper(start[1:], goal[1:], limit, counter+1)
    # return halper(start, goal, limit, chenge_count)


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    # print("DEBUG:", start, goal, limit)
    if start == '' or goal == '' or limit < 0:  # Fill in the condition
        # BEGIN PROBLEM 7
        return abs(len(goal) - len(start))
        # END PROBLEM 7

    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN PROBLEM 7
        return pawssible_patches(start[1:], goal[1:], limit)
        # END PROBLEM 7

    else:
        add_diff = pawssible_patches(goal[0]+start, goal, limit-1)
        remove_diff = pawssible_patches(start[1:], goal, limit-1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1)
        # BEGIN PROBLEM 7
        return min(add_diff, remove_diff, substitute_diff) + 1
        # END PROBLEM 7


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    i = 0
    while i < len(typed):
        if typed[i] != prompt[i]:
            break
        i += 1
    accuracy_num = i / len(prompt)
    user_info = {'id': user_id, 'progress': accuracy_num}
    send(user_info)
    return accuracy_num
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    for player in range(len(times_per_player)):
        for word in range(len(times_per_player[player])-1, 0, -1):
            times_per_player[player][word] -= times_per_player[player][word-1]
    times = [player_tiems[1:] for player_tiems in times_per_player]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    # contains an *index* for each player
    player_indices = range(len(all_times(game)))
    # contains an *index* for each word
    word_indices = range(len(all_words(game)))
    # BEGIN PROBLEM 10
    word_fastest = list(word_indices)
    for word in word_indices:
        min_time = time(game, 0, word)
        min_index = 0
        for player in player_indices:
            if time(game, player, word) < min_time:
                min_time = time(game, player, word)
                min_index = player
        word_fastest[word] = min_index
    # print("DEBUG:", word_fastest)
    player_fastest_list = \
        [[word_at(game, word) for word in word_indices
          if word_fastest[word] == player]
         for player in player_indices]
    return player_fastest_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
               for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
