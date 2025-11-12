def view_person(name,age,*friends,love="Mother",**perspective):
    print(name,age)
    print(friends,"->they were friends")
    print('love of my life->',love)
    print(perspective)

view_person('chetan',26,'vyshak','rakshith','kishore','sneha',aim='moksha',hobby='spiritual_talk',interest='arm_wrestling')

