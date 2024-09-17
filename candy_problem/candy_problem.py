friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_favorite_candy_count(favorites):
    candy_dict = {}
    for friend_candies in favorites:
        candies = friend_candies[1]
        for candy in candies:
            if candy not in candy_dict:
                candy_dict[candy] = 1
            else:
                candy_dict[candy] += 1
    return candy_dict
    
'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    fav_candy_dict = {}
    for friend_candies in data:
        friend = friend_candies[0]
        candies = friend_candies[1]
        
        for candy in candies:
            if candy not in fav_candy_dict:
                fav_candy_dict[candy] = []
                fav_candy_dict[candy].append(friend)
            else:
                fav_candy_dict[candy].append(friend)
    # print(fav_candy_dict)
    return fav_candy_dict


# create_new_candy_data_structure(friend_favorites)

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    fav_candy_dict = create_new_candy_data_structure(data)
    if candy_name not in fav_candy_dict:
        return ()
    friends_who_like_candy = fav_candy_dict[candy_name]
    friends_who_like_candy = tuple(friends_who_like_candy)
    # print(friends_who_like_candy)
    return friends_who_like_candy

get_friends_who_like_specific_candy(friend_favorites, "lollipop")

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    fav_candy_dict = create_new_candy_data_structure(data)
    fav_candy_dict = set(fav_candy_dict)
    return fav_candy_dict

create_candy_set(friend_favorites)
'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

