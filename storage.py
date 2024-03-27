            for inner_key, inner_values in outer_value.items():
                # DID SOMEONE SEND A DICTIONARY INSIDE A DICTIONARY INSIDE A DICTIONARY?!
                if isinstance(inner_values, dict):
                    # Loop the inner most dictionary
                    for innerest_key, innerest_value in inner_values.items():
                        if isinstance(innerest_value, dict):
                            print("You've dug too deep, go back greedy dwarf.")
                            return False
                        else:
                            print(f"Key: {innerest_key}, Value: {innerest_value}")
                else:
                    # print(f"Key: {inner_key}, Value: {inner_values}")
                    pass
