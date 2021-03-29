# Mitchell Blake, Student ID:#001688874
import csv
from HashTable import HashTable
from datetime import datetime, timedelta

# TOTAL TIME COMPLEXITY OF ENTIRE PROGRAM:O(m^2)
# hash table class has time complexity of O(m*n) and major blocks within the main program have
# O(m^2) as largest complexity, this makes the entire program a complexity of O(m^2)
#
# TOTAL SPACE COMPLEXITY OF ENTIRE PROGRAM:O(m^2*n^2)
# hash table class has a space complexity of O(m*n) and major blocks within the main program have
# O(m^2*n^2) as the largest complexity, this makes the entire program a complexity of O(m^2*n^2)

distances = HashTable(27)

# TOTAL TIME COMPLEXITY FOR CODE BLOCK: O(m*n) multi-linear
# TOTAL SPACE COMPLEXITY FOR CODE BLOCK: O(m*n) multi-linear

# build a distance hashtable from the distance csv for path use
with open(r'distances.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    # we need to skip the first 8 rows which are irrelevant to our data collection
    for row in range(7):
        next(reader)
    # create a dict reader object
    # TIME COMPLEXITY: O(m * n) multi-linear
    # dict reader
    # m = rows of information read
    # n = columns of information read
    #
    # Specific time complexity should then be equal to 2(m * n) which can be consider O(m*n)
    # SPACE COMPLEXITY: O(z*m*n) multi-linear
    # dictReader
    # for each row (Z) we have (n) columns with variable length strings (m)
    # each dictionary is representative of a row and the columns within that row.
    # 1 byte per character for each column string within a row times the amount of rows.
    # space complexity for dict-reader object is equal to Z(m*n) multi-linear complexity
    my_dict = csv.DictReader(csvfile)
    # index will start at 2 for address value columns
    index = 2
    # list for rows of distance csv to match with column addresses
    # SPACE COMPLEXITY:O(n) linear
    # rows list
    # 1 byte per character of the string which will be added to the rows list
    # each string added to the rows list will vary so we have
    # stringLength = s, rows = r.(s1 +s2 +s3...r)
    # the sum of each character string in the list added together.
    # rows has linear complexity because each string added increase the length of the row by 1
    rows = []
    # TIME COMPLEXITY LOOPS: O(m*n) multi-linear
    # the for loops have a time complexity of O(m * n) with n being the size of the item iterable list
    # and m being the size of the dictionary within the iterable list.
    # for each item in the item iterable list we have a nested for loop.
    # the nested for loop iterates over each key within the dictionary at the index of the item iterable list
    # if the length of the item iterable list = n
    # then each dictionary within the iterable list has a length = m
    # both the length of the item and the dictionary within the item can be different

    # SPACE COMPLEXITY LOOPS: O(m*n) for each item(n) in the dict reader object each variable(v)/list(l)
    # or hash table(h) is created (l + v + h )* n = O(m*n)

    for item in my_dict:
        # create list of columns representing a row of information
        # columns list has a space complexity of (n*m) because it is a list of keys(columns) generated for each
        # item within the dict reader object. every iteration of the for loop will create a column list of length m
        columns = list(item)

        # build our distances hashtable one element at a time
        # assignment of distances hash table keys is linear O(n) it only happens once per loop iteration.
        location = item.get('DISTANCE BETWEEN HUBS IN MILES')
        if location != columns[index]:
            location = item.get('HUB')

        distances.insert(location, [location, item.get(columns[index])])
        # create our row list to match with column list
        rows.append(location)

        keyCol = 0
        for key, value in item.items():
            # we can quit if we have reached the column which represents the same address as our row
            if key == location:
                break
            if keyCol >= 2 and key == columns[keyCol]:
                # add to our distances each value which is associated with a specific key
                # our columns are ahead by 2 because of the distance and hubs columns within the item dictionary
                # subtracting 2 from keyCol value will allow a match of address values by row and col.
                # SPACE COMPLEXITY: O(m*n)
                # assignment of distance hash table values is multi-linear O(M * N) for each column(n) in the dictionary
                # of the current loop a value will be assigned to the hashtable  row(m)
                distances.get(rows[keyCol - 2]).append([location, value])  # pull data vertically and add to hash table
                distances.get(location).append([rows[keyCol - 2], value])  # pull data horizontally and add to hashtable
            # prepare to pull next address data for hashtable
            # advance col to next address
            keyCol += 1

        # index is keeping track of which column/row combination we should be on
        index += 1

packages = HashTable(40)

# TOTAL TIME COMPLEXITY FOR CODE BLOCK: O(m*n) multi-linear
# TOTAL SPACE COMPLEXITY FOR CODE BLOCK: O(m*n) multi-linear

# build a package hashtable from the package csv for status and updates
with open(r'packages.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in range(7):
        next(reader)
    # TIME COMPLEXITY: O(m * n)
    # dict reader
    # m = rows of information read
    # n = columns of information read
    # SPACE COMPLEXITY: O(z*m*n)
    # dictReader
    # has a space complexity of (Z*m*n)
    # for each row (Z) we have (n) columns with variable length strings (m)
    # each dictionary is representative of a row and the columns within that row.
    # 1 byte per character for each column string within a row times the amount of rows.
    # space complexity for dict-reader object is equal to (Z*m*n) multi-linear complexity
    my_dict = csv.DictReader(file)
    # iterate through values provided by dict reader
    #
    # TIME COMPLEXITY LOOPS: O(m*n)
    # the for loops have a time complexity of O(m * n) with n being the size of the item iterable list
    # and m being the size of the dictionary within the iterable list.
    # for each item in the item iterable list we have a nested for loop.
    # the nested for loop iterates over each key within the dictionary at the index of the item iterable list
    # if the length of the item iterable list = n
    # then each dictionary within the iterable list has a length = m
    # both the length of the item and the dictionary within the item can be different
    # Specific time complexity should then be equal to 2(m * n) which can be consider O(m*n)
    #
    # SPACE COMPLEXITY LOOPS: O(m*n)
    # for each iteration of the my_dict list we have a packageKeys list(l) of length n.
    # a package val list(vl) of length n, which is (l*n) + (vl*n) for a complexity of 2(m*n) or O(m*n)
    for item in my_dict:
        # create a list from the keys of our item dictionary
        # SPACE COMPLEXITY: O(n*m)
        # packageKeys list has a space complexity of (n*m) because it is a list of keys generated for each
        # item(n) within the dict reader object. every iteration of the for loop will create a
        # packageKey list of length m
        packageKeys = list(item)
        # we want to build a list consisting of package data

        # SPACE COMPLEXITY:O(n*m)
        # assignment of package list is multi-linear O(n*m) it happens once per loop iteration.
        # has a length equal to the amount of columns in the csv file.
        packageVal = []
        for col in range(8):
            if col == 3:  # skip state data because it is not required
                continue
            # add the data pulled from each column from 0-7 skipping 3
            packageVal.append(item.get(packageKeys[col]))

        # update the address info for package 9
        if packageVal[0] == '9':
            packageVal[1] = '410 S State St'
            packageVal[3] = '84111'

        # copy the packageVal list to be used as a key in our hash table
        packageKey = packageVal.copy()
        packageVal.append('at the hub')
        packageKey.append('status')
        packageKey.append('delivery truck')
        packageVal.append('unknown')
        packageKey = tuple(packageKey)
        # add the key, value pair to hash table
        packages.insert(packageKey, packageVal)


# TOTAL TIME COMPLEXITY for get_path function: O(m^2) quadratic
# TOTAL SPACE COMPLEXITY for get_path function: O(m^2*n^2) multi-linear quadratic

# get path for delivery truck, provides updates and pseudo time for delivery checks
def get_path(truck, start_hour, start_min, end_hour, end_min, truck_name):
    # assign starting hub location and initial values
    start = ' 4001 South 700 East'
    my_sum = 0
    curr_hub = start
    shortest = 100
    path = []
    next_hub = None
    remove_packages = []
    update_packages = []
    # get the time our packages will leave the hub
    curr_time = datetime(2021, 3, 17, hour=start_hour, minute=start_min)
    # get the time our user wants data for
    moment = datetime(2021, 3, 17, hour=end_hour, minute=end_min)

    # run simulation while packages are in our truck
    # TIME COMPLEXITY LOOPS: O(m^2) quadratic
    # m is the iterations of the outer while loop which iterates over the packages in the truck.
    # m is the iterations of the for loop within the while loop which also iterates over the packages in the truck.
    # there is another loop found in a list comprehension within the first for loop which iterates over values(p)
    # which are found within the packages hash table
    # n is the iterations of the third for loop within the former for loop which iterates over distances.
    # (m* m * p * n) is the time complexity of the loops which can be consider O(n*p *m^2) quadratic
    # SPACE COMPLEXITY LOOPS: O(m^2*n^2) quadratic
    # while loop iterates n times, for loop also iterates n times. variable lists package_info and package_chk of length
    # (m) are generated (n^2 * m^2), address lists with length a are generated (n^2 * a) times, update and remove
    # package lists are generated (n^2*r) and (n^2*u). total space complexity = (n^2*m^2*r*u) = (n^2*m^2)
    while truck:
        if moment < curr_time:
            return 0, curr_time

        for package in truck:
            # SPACE COMPLEXITY:)O(n^2*m^2) quadratic
            # a package_info list and package_chk tuple of length (m), is created for each for loop of length(n)
            # within each while loop of length(n).(n^2*m^2)
            package_info = [keys for keys, vals in packages.items() if package == vals[0]]
            package_chk = tuple(package_info[0])

            # assign current time to package
            minute = f'{curr_time.minute}'
            if curr_time.minute < 10:
                minute = f'0{curr_time.minute}'

            packages.get(package_chk)[7] = f'en route {curr_time.hour}:{minute}'
            packages.get(package_chk)[8] = truck_name
            # SPACE COMPLEXITY:O(n^2) quadratic
            # an address list of length v is created for each for loop within each while loop.(n^2*v)
            address = [keys for keys, vals in distances.items() if
                       str(package_info[0][1]) in keys]  # change package address to distance address

            # if there is no data in the address list something went wrong
            # slice the package address name down to a smaller string and see if it can be found in
            # the distances address names
            # SPACE COMPLEXITY:O(n^2) quadratic
            # if an address is not found the if not address condition must execute and build another address list
            # this list can be built at most (n^2) times with a variable length (a) which makes a (n^2*a)
            # space complexity
            if not address:
                slice_address = str(package_info[0][1])[:5]
                address = [keys for keys, vals in distances.items() if slice_address in keys]
            hub_address = address[0]

            # keep packages delivered at same address in a group if address is nearest neighbor
            if hub_address == next_hub:
                remove_packages.append(package)
                update_packages.append(package_chk)
                continue

            # find distance from current location to location of next package in truck and find
            # if it is the nearest neighbor
            hub = distances.get(hub_address)
            # SPACE COMPLEXITY: O(n^2) quadratic
            # remove packages (r) and update packages(u) are created at most n^2 times which is a space complexity of
            # (n^2*r) and (n^2*u).
            for my_index in range(2, 28):
                if hub[my_index][0] == curr_hub:
                    if float(hub[my_index][1]) < shortest:
                        shortest = float(hub[my_index][1])
                        next_hub = hub_address
                        remove_packages.clear()
                        remove_packages.append(package)
                        update_packages.clear()
                        update_packages.append(package_chk)
                        break

        # build our path consisting of packages/next hub location/ the distance traveled to next hub location
        path.append([remove_packages.copy(), next_hub, shortest])
        my_sum += shortest

        # remove packages that were delivered from the truck
        for package in remove_packages:
            truck.remove(package)

        # calculate minutes passed from last delivery
        count_minutes = shortest / 18 * 60
        add_minutes = timedelta(minutes=count_minutes)
        curr_time = curr_time + add_minutes

        # if we have passed user time deadline quit the program and packages in current iteration are
        # not marked as being delivered otherwise mark as delivered and continue to next iteration
        if curr_time > moment:
            return my_sum, curr_time
        elif curr_time <= moment:
            for package in update_packages:
                minute = f'{curr_time.minute}'
                if curr_time.minute < 10:
                    minute = f'0{curr_time.minute}'
                packages.get(package)[7] = f'delivered {curr_time.hour}:{minute}'

        curr_hub = next_hub
        shortest = 100
        next_hub = None

        # if we have delivered all packages in truck, we need to add distance back to start hub
        if not truck:

            hub = distances.get(curr_hub)
            for my_index in range(2, 28):
                if hub[my_index][0] == start:
                    wgu_hub = float(hub[my_index][1])
                    path.append([-1, -1, wgu_hub])
                    my_sum += wgu_hub

    return my_sum, curr_time, path


exit_program = False
# TOTAL TIME COMPLEXITY: O(m^2) quadratic
# get_path function has time complexity of O(m^2)
# get_path is called three times per iteration of outer while loop.
# each while user input loop(u) is called once per iteration of the outer while loop(k)
# time complexity will be equal to (u * k * m^2) = (m^2)
#
# TOTAL SPACE COMPLEXITY: O(n^2*m^2) quadratic
# get_path has space complexity of O(m^2*n^2)
# get_path is called three times per iteration of outer while loop
# get_path has largest space complexity in the loop so the space complexity of the whole code block is equal
# to (m^2*n^2)

# user interface and input
while not exit_program:
    # user entry for time value to check status of packages
    user_time = input('please enter hours and minutes of a time in military format. "HH:mm" ex.(16:34)')
    user_end = user_time.split(":")
    while len(user_end) > 2 or len(user_end[0]) > 2 or len(user_end[1]) > 2 or (int(user_end[0]
                                                                                    ) > 23 or int(user_end[0]) < 0) or (
            int(user_end[1]) > 59 or int(user_end[1]) < 0):
        user_time = input(
            'please reenter time in format "HH:mm", hour values 0-23 and minute values 0-59 w/out leading zeroes ')
        user_end = user_time.split(":")

    # user enter the kind of query. User may request package list by id,status,address,etc.
    user_package = input('please enter a package id(1-40) or "0" for all packages, or other package property/status ')
    # both weight and status must be explicitly specified in lookup function so user
    # verifies whether they have been entered.
    is_weight = input('was weight entered as package property? y/n ')
    is_status = input("was a status ie(delivered,at the hub, en route) entered as package property? y/n ")
    while is_weight != 'y' and is_weight != 'n':
        is_weight = input("you must enter 'y' or 'n' for whether a weight property was entered as search parameter. ")

    if is_weight == 'y':
        is_weight = True
    else:
        is_weight = False

    if is_status == 'y':
        is_status = True
    else:
        is_status = False

    # TIME COMPLEXITY: O(m^2) quadratic
    # get_path function has time complexity of O(m^2)
    # get_path is called three times per iteration of the while loop. 3(m^2)
    # time complexity = (m^2)
    # SPACE COMPLEXITY = O(m^2 * n^2) quadratic
    # get_path has a space complexity of m^2*n^2 and is called 3 times
    # for a specific complexity of 3(m^2*n^2)
    # space complexity = (m^2*n^2)

    # load trucks with packages and run simulation
    truck1 = ['14', '15', '19', '16', '13', '20', '21', '12', '6', '32', '34', '31', '39', '22', '4', '40']
    truck2 = ['3', '18', '36', '38', '33', '2', '28', '1', '26', '25', '37', '8', '30', '5', '29', '7']
    res = get_path(truck1, 8, 0, int(user_end[0]), int(user_end[1]), 'truck1')
    res2 = get_path(truck2, 9, 5, int(user_end[0]), int(user_end[1]), 'truck2')  # hold truck until 09:05
    truck3 = ['9', '10', '17', '27', '35', '24', '23', '11']
    res3 = get_path(truck3, 10, 20, int(user_end[0]), int(user_end[1]), 'truck3')  # hold truck until 10:20
    res_sum = res[0] + res2[0] + res3[0]

    # get a list of a single package or all packages
    my_packages = []
    if user_package != '0':
        deliveries_status = True
        # lookup package by weight
        if is_weight:
            my_packages = packages.lookup(weight=user_package)

        # lookup package by status(delivered,at the hub,or en route)
        elif is_status:
            my_packages = packages.lookup(status=user_package)

        # lookup package with id,address,city,zip
        else:
            my_packages = packages.lookup(user_package)

    elif user_package == '0':
        for key, val in packages.items():
            my_packages.append(val)

    # TIME COMPLEXITY LOOP: O(n*m) multi-linear
    # for each package in the my_packages list values are printed n times
    #
    # SPACE COMPLEXITY LOOP: O(n*m*s) multi-linear
    # for each package in the my_packages list values are printed n times with string length of s

    # print values for query
    count = 0
    for val in my_packages:
        # update packages marked 'at the hub' with the time of user requested query
        if val[6] == 'at the hub':
            val[6] = f'at the hub {user_end[0]}:{user_end[1]}'
        special_notes = val[6]
        if not special_notes:
            special_notes = 'None'

        if 'delivered' in val[7]:
            count += 1

        # print matching package information
        print(f"\npackageId: {val[0]}, Address: {val[1]}, City: {val[2]}, Zip: {val[3]}, DeliverDeadline: {val[4]},"
              f" Weight: {val[5]},SpecialNotes:{special_notes}, DeliveryStatus: {val[7]}, DeliveryTruck:{val[8]}")

        if count == 40:
            print("\nAll packages delivered.")
    # something went wrong pulling data for user query
    if not my_packages:
        print("\nno information was found for your requested package inquiry.")
        print("this may be a mistake due to your input.")
        print("if you are searching for a package id, the input must be 1-40")
        print("if you are searching by zip,city,deadline,or status be sure it is inputted according to requirements")

    # print truck miles traveled and ask if user wants out of program
    print(f"total mileage for all trucks = {res_sum}")
    print(f" at {user_end[0]}:{user_end[1]}")
    my_quit = input("are you finished with the program? y/n ")

    # check if user wants out of program
    if my_quit == 'y':
        exit_program = True
    else:
        exit_program = False
