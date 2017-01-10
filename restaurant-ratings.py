# your code goes here

def convert_file_to_dict(filename):
    file_ref = open(filename)
    rest_ratings = {}

    for line in file_ref:     
        rest_name, rest_score = line.rstrip().split(':')
        rest_ratings[rest_name] = rest_score

    file_ref.close()

    return rest_ratings


def get_sort_dictionary(dictionary):
    """ Sorting resturaunts alphabetically and creating a dictionary
    of restaurants with their corresponding score.
    """
#    rest_ratings = convert_file_to_dict('scores.txt')
    #try:    
    for name, score in sorted(dictionary.items()):
        print name + ' is rated at ' + str(score) + '.'
    #except:
        #"A mistake somewhere..."

existing_dict = convert_file_to_dict('scores.txt') 


custom_rest = raw_input("Please choose a restaurant: ").title()


if custom_rest in existing_dict:
    custom_ans = raw_input("This restaurant is already rated. Would you like to change the score? Y/N: ").upper()
    
    if custom_ans == 'Y':
        custom_score = int(raw_input("Please score chosen restaurant: "))
       
    
    elif custom_ans == 'N':
        custom_rest = raw_input("Please choose a restaurant: ").title()
        custom_score = int(raw_input("Please score chosen restaurant: "))

else:
     custom_score = int(raw_input("Please score chosen restaurant: "))

existing_dict[custom_rest] = custom_score
get_sort_dictionary(existing_dict)
