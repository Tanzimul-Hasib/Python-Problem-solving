
result=0
basket_items={'apples':4,'oranges':19,'kites':3,'sandwiches':8}
fruits=['apples','oranges','pears','peaches','grapes','bananas']
for key ,value in basket_items.items():
        if key in fruits :
            result += value

print(result)
