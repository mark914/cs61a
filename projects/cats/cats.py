"""Typing test implementation"""

from os import kill, stat_result
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
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    vaild_paragraphs = []
    for paragraph in paragraphs:
        if select(paragraph):
            vaild_paragraphs.append(paragraph)

    if len(vaild_paragraphs) <= k:
        return ''
    else:
        return vaild_paragraphs[k]



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
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    def select(paragraph):
        if paragraph in topic:
            return True
        return False
    return select

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
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    denom = len(typed_words)
    refer_len = len(reference_words)
    if denom == 0:
        return 0.0
    if denom > refer_len:
        typed_words = typed_words[:refer_len]
    else:
        reference_words = reference_words[:denom]
    
    sum = 0
    for i in range(len(typed_words)):
        if typed_words[i] == reference_words[i]:
                sum += 1
    return sum/denom*100

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4

    typed_num = 0
    for _ in typed:
        typed_num += 1

    return typed_num/(5*elapsed)*60


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        diff = [diff_function(user_word, valid_word,limit) for valid_word in valid_words]
        if min(diff) > limit:
            return user_word
        else:
            for valid_word in valid_words:
                if diff_function(user_word, valid_word,limit) == min(diff):
                    return valid_word
                    
            


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    #要有能够记录错误数目的变量k
    def help(start, goal, limit, k):
        if k+abs(len(start)-len(goal)) > limit:
            return limit+1
        #base case    
        if start == '' or goal == '':
            return k+abs(len(start)-len(goal))  if k+abs(len(start)-len(goal))<=limit else limit+1
        else:#recursion case
            if start[0] == goal[0]:
                return help(start[1:], goal[1:], limit, k)
            else:
                return help(start[1:], goal[1:], limit, k+1)

    return help(start, goal, limit, k=0)





def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    # def help(start, goal, limit, k):
    #     if k+abs(len(start)-len(goal)) > limit:
    #         return limit+1

    #     if len(start) == 1:
    #         if len(goal) == '':
    #             return k+1
    #         elif goal[0] == start[0]:
    #             return k+abs(len(start)-len(goal))
    #         elif goal[0] != start[0]:
    #             return k+abs(len(start)-len(goal))+1

    #     elif len(goal) == 1:
    #         if len(start) == '':
    #             return k + 1
    #         elif goal[0] == start[0]:
    #             return k+abs(len(start)-len(goal))
    #         elif goal[0] != start[0]:
    #             return k+abs(len(start)-len(goal))+1
         
    #     else:
    #         if start[0] == goal[0]:  #the same
    #             return help(start[1:], goal[1:], limit, k)
    #         elif start[0] == goal[1]: #add
    #             return help(start, goal[1:], limit, k+1)
    #         elif start[1] == goal[0]: #delet
    #             return help(start[1:], goal, limit, k+1)
    #         elif start[1] == goal[1]: #substitute
    #             return help(start[1:], goal[1:], limit, k+1)

    return help(start, goal, limit, k=0)






def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    #一定要想清楚什么时候能够进入if条件，如果没有输出，以为着语句没有执行。意味着条件不符合。
    number = 0
    for i in range(len(typed)):
        if typed[i] != prompt[i]:
            break
        number += 1

    progress = number/len(prompt) 
    send({'id':user_id, 'progress':progress})
    return progress

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
    "*** YOUR CODE HERE ***"
    times = []
    for player in times_per_player:
        player_times = []
        for i in range(len(player)-1):
            player_times.append(player[i+1]-player[i])
        times.append(player_times)   
    # print(times)
    return game(words, times)





    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10
    #思路很重要，你要如何去构建一个list of lists，满足什么条件才添加一个元素。
    word_times = []
    for i in word_indices:
        word_time = []
        for j in player_indices:
            word_time.append(time(game, j, i))
        word_times.append(word_time)  

    fast = []
    for i in player_indices:
        fast_player = []
        for j in word_indices:
            if time(game, i, j) == min(word_times[j]):
                fast_player.append(word_at(game, j))
                word_times[j].append(0)  #当平局的时候，判定index小的player最快

        fast.append(fast_player)        
    
    return fast








def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
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
    select = lambda p: True
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