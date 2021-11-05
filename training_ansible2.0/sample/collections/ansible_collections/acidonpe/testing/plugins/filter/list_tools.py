def list_split(orig_list, items):
    '''
    This plugin receive an array and split them in n blocks
    '''    
    if not isinstance(orig_list, list):
        raise TypeError("Input provided is not a list")
    
    # Number of input array positions
    array_len = len(orig_list)

    if items > array_len:
        raise TypeError("Number of items if higher than array positions")

    elif items == 0 or items == array_len:
        return orig_list

    else:
        # final list to return
        final_list = []

        # Generate chunks
        for i in range(0, array_len, items):
            final_list.append(orig_list[i:i + items])

        return final_list

class FilterModule(object):
    def filters(self):
        return {
            'list_split': list_split
        }
