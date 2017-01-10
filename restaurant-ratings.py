# your code goes here


def get_sorted_resturaunts(filename):
    """ Sorting resturaunts alphabetically and creating a dictionary
    of restaurants with their corresponding score.
    """
    
    file_ref = open(filename)
    rest_ratings = {}

    for line in file_ref:
        
        rest_name, rest_score = line.rstrip().split(':')

        rest_ratings[rest_name] = rest_score
    

    file_ref.close()


    for restaurant, score in sorted(rest_ratings.items()):
        print restaurant + ' is rated at ' + score + '.'



get_sorted_resturaunts('scores.txt')

