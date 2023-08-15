# Michael Thomas Student ID:001401671

import sys, datetime, time

class HastTable:
    def __init__(self):
        self.Max = 10
        self.hash_table = [[] for i in range(self.Max)]

    # This uses the package_id to create a hash key
    def get_hash(self, key):
        return key % self.Max

    # The package_id is the key
    def add_item(self, package_id, address, city, state, zip_code, deadline, kilos, notes, status):
        hash_key = self.get_hash(package_id)
        entry = {'p_id': package_id, 'address': address, 'city': city, 'state': state,
                 'zip_c': zip_code, 'deadline': deadline, 'kilos': kilos, 'notes': notes, 'status': status,
                 'delivery_time': datetime.datetime(2022, 11, 2, 0, 0)}

        # This just appends items to the hash location so no collisions occur
        self.hash_table[hash_key].append(entry)

    # This returns the item in the hash table
    def get_item(self, key):
        hash_key = self.get_hash(key)

        # This searches through the entries at this index to return the item with the same key(package_id/'p_id')
        for i in range(len(self.hash_table[hash_key])):
            this = self.hash_table[hash_key][i]
            if this['p_id'] == key:
                return self.hash_table[hash_key][i]

class Graph:

    graph = {}

    def add_node(self, address, node):
        self.graph[address] = node

    def add_distance(self, name_list_i, name_list_j):
        self.graph[name_list_j][name_list_i] = self.graph[name_list_i][name_list_j]

    def get_distance(self, address_from, address_to):
        return self.graph[str(address_from)][str(address_to)]

def nearest_neighbor(truck):
    g = Graph()
    sorted_truck = []
    unsorted_truck = truck
    current_location = '4001 South 700 East'
    min_length = 100
    restart_1 = False
    restart_2 = False
    final_loops = False
    remove_index = None

    while len(unsorted_truck) > 0 :

        # This finds the nearest neighbor with time contraints
        nearest = unsorted_truck[0]
        for i in range(len(unsorted_truck)):
            pk = unsorted_truck[i]

            if pk['deadline'] < datetime.time(10,00):
                if g.graph[current_location][pk['address']] < min_length:
                    nearest = pk
                    min_length = g.graph[current_location][pk['address']]
                    remove_index = i
                    restart_1 = True

        if restart_1 == True:
            sorted_truck.append(nearest)
            unsorted_truck.pop(remove_index)
            current_location = nearest['address']

            min_length = 100
        if restart_1 == False:

            for i in range(len(unsorted_truck)):
                pk = unsorted_truck[i]

                if pk['deadline'] < datetime.time(11, 00):
                    if g.graph[current_location][pk['address']] < min_length:
                        nearest = pk
                        min_length = g.graph[current_location][pk['address']]
                        remove_index = i
                        restart_2 = True

            if restart_2 == True:
                sorted_truck.append(nearest)
                unsorted_truck.pop(remove_index)
                current_location = nearest['address']
                min_length = 100

            else:
                final_loops = True

        if final_loops == True:
            for i in range(len(unsorted_truck)):
                pk = unsorted_truck[i]

                if g.graph[current_location][pk['address']] < min_length:
                    nearest = pk
                    min_length = g.graph[current_location][pk['address']]
                    remove_index = i

            sorted_truck.append(nearest)
            unsorted_truck.pop(remove_index)
            current_location = nearest['address']
            min_length = 100


        restart_1 = False
        restart_2 = False

    # This finds the nearest neighbor of packages that do not have time restraints

    return sorted_truck

def search_main(num, search_c, truck_1, truck_2, truck_3):

    search_list = []

    def search(truck, search_criterea, search_category):
        for i in range(len(truck)):
            truck_package = truck[i]
            if truck_package[search_category] == search_criterea:
                search_list.append(str(truck_package).strip('{').strip('}'))

    if int(num) == 1:
        search_list.clear()
        id_entry_text = int(search_c)

        search(truck_1, id_entry_text, 'p_id')
        search(truck_2, id_entry_text, 'p_id')
        search(truck_3, id_entry_text, 'p_id')

    if int(num) == 2:
        search_list.clear()
        address_entry_text = search_c

        search(truck_1, address_entry_text, 'address')
        search(truck_2, address_entry_text, 'address')
        search(truck_3, address_entry_text, 'address')

    if int(num) == 3:
        search_list.clear()
        deadline_entry_text = search_c
        t_parts = time_format.split(':')
        dline = datetime.time(int(t_parts[0]), int(t_parts[1]))

        search(truck_1, dline, 'deadline')
        search(truck_2, dline, 'deadline')
        search(truck_3, dline, 'deadline')

    if int(num) == 4:
        search_list.clear()
        city_entry_text = search_c

        search(truck_1, city_entry_text, 'city')
        search(truck_2, city_entry_text, 'city')
        search(truck_3, city_entry_text, 'city')

    if int(num) == 5:
        search_list.clear()
        zip_entry_text = int(search_c)

        search(truck_1, zip_entry_text, 'zip_c')
        search(truck_2, zip_entry_text, 'zip_c')
        search(truck_3, zip_entry_text, 'zip_c')

    if int(num) == 6:
        search_list.clear()
        kilos_entry_text = int(search_c)

        search(truck_1, kilos_entry_text, 'kilos')
        search(truck_2, kilos_entry_text, 'kilos')
        search(truck_3, kilos_entry_text, 'kilos')

    if int(num) == 7:
        search_list.clear()
        status_entry_text = search_c

        search(truck_1, status_entry_text, 'status')
        search(truck_2, status_entry_text, 'status')
        search(truck_3, status_entry_text, 'status')

    #This displays the search results
    if len(search_list) > 0:
        print(str(len(search_list)) + ' results returned')
        for i in range(len(search_list)):
            print('\n' + str(search_list[i]))

    else:
        print('No search results found')

if __name__ == '__main__':

    # This block get the addresses from the file to be used as the names for the node dictionary
    name_list = []
    #with open("C:\\Users\\tyler_ovixfls\\Downloads\\WGUPS Distance Table - Sheet1.csv", "r") as distance_table:
    with open("WGUPS Distance Table - Sheet1.csv", "r") as distance_table:
        for line in distance_table:

            tokens = line.split(',')
            comma_count = len(tokens)

            for i in range(comma_count):
                thing = tokens[i].strip().strip("\"")
                if i == 1:
                    name_list.append(thing)

    # This block gets the values to be added to the node dictionary.
    # After each line adds the node dictionary to the graph.
    #graph = {}
    g = Graph()
    #with open("C:\\Users\\tyler_ovixfls\\Downloads\\WGUPS Distance Table - Sheet1.csv", "r") as distance_table:
    with open("WGUPS Distance Table - Sheet1.csv", "r") as distance_table:
        # This reads in from file and splits data at the commas
        for line in distance_table:
            tokens = line.split(',')
            comma_count = len(tokens)

            node = {}

            for i in range(comma_count):

                    thing = tokens[i].strip().strip("\"")
                    if i == 1:
                        address = thing
                    if i > 2 and i < 30:
                        if len(thing) > 0:
                            node[name_list[i - 3]] = float(thing)
                        else:
                            node[name_list[i - 3]] = sys.maxsize

            #graph[address] = node
            g.add_node(address, node)
            del node

    # This fills in the rest of the graph("distance table")
    for i in range(len(name_list)-1, -1, -1):
        for j in range(len(name_list)):
            g.add_distance(name_list[i], name_list[j])

    # This code block reads data in from the package file.
    #Then it puts the package data into a hash function in the class created above
    ht = HastTable()

    with open("Copy of WGUPS Package File - Sheet11.csv", "r") as package:
        for line in package:

            tokens = line.split(',')
            package_id = int(tokens[0])
            address = tokens[1]
            city = tokens[2]
            state = tokens[3]
            zip_code = int(tokens[4])
            kilos = int(tokens[6])
            notes = tokens[7]

            # This block handle creating a time object
            if tokens[5] == 'EOD':
                deadline = datetime.time(20, 00)
            else:
                time_format = tokens[5].strip(' AM')
                time_parts = time_format.split(':')
                deadline = datetime.time(int(time_parts[0]), int(time_parts[1]))

            ht.add_item(package_id, address, city, state, zip_code, deadline, kilos, notes, 'at the hub')

    #This block puts the packages on the truck
    truck_1 = []
    truck_2 = []
    truck_3 = []

    # This creates a list of packages at the hub that have not been put on trucks
    items_at_hub = []
    for i in range(1, 41):
        items_at_hub.append(i)

    # This handles package with early deadlines (before 10:00 AM)
    for i in items_at_hub[:]:
        pk = ht.get_item(i)
        if pk['deadline'] < datetime.time(10, 00):
            truck_1.append(pk)
            items_at_hub.remove(i)

    # This handles packages with later deadline (before 11:00 AM)
    for i in items_at_hub[:]:
        pk = ht.get_item(i)

        # This block handles packages with time constraints
        if pk['deadline'] < datetime.time(11, 00) and len(truck_2) < len(truck_1):
            truck_2.append(pk)
            items_at_hub.remove(i)

        elif pk['deadline'] < datetime.time(11, 00):
            truck_1.append(pk)
            items_at_hub.remove(i)

    # This block handles packages with notes
    for i in items_at_hub[:]:
        pk = ht.get_item(i)

        # This block handles special notes
        notes = pk['notes']
        if notes != '\n':
            if pk['notes'] == 'Can only be on truck 2\n':
                truck_2.append(pk)
                items_at_hub.remove(i)

            elif pk['notes'] == 'Delayed on flight---will not arrive to depot until 9:05 am\n':
                if pk['deadline'] <= datetime.time(11, 00):
                    truck_2.append(pk)
                    items_at_hub.remove(i)
                else:
                    truck_3.append(pk)
                    items_at_hub.remove(i)

            elif 'Must be delivered with' in pk['notes']:
                truck_2.append(pk)
                items_at_hub.remove(i)

    # This block selects the truck if there are no notes or deadlines
    for i in items_at_hub[:]:
        pk = ht.get_item(i)

        if len(truck_1) <= len(truck_2) and len(truck_1) < 16:
            truck_1.append(pk)
            items_at_hub.remove(i)

        elif len(truck_2) < len(truck_1) and len(truck_2) < 16:
            truck_2.append(pk)
            items_at_hub.remove(i)

        else:
            truck_3.append(pk)
            items_at_hub.remove(i)

    # This block sorts the packages in the trucks to find the shortest route
    truck_1 = nearest_neighbor(truck_1)
    truck_2 = nearest_neighbor(truck_2)
    truck_3 = nearest_neighbor(truck_3)

    truck_1_time = datetime.datetime(2022, 11, 2, 8)
    truck_2_time = datetime.datetime(2022, 11, 2, 9, 5)
    truck_3_time = datetime.datetime(2022, 11, 2, 8)

    truck_1_distance = 0
    truck_2_distance = 0
    truck_3_distance = 0

    first_truck_location = '4001 South 700 East'
    second_truck_location = '4001 South 700 East'
    third_truck_location = '4001 South 700 East'

    truck_1_count = 0
    truck_2_count = 0
    truck_3_count = 0

    truck_1_at_the_hub = True
    truck_2_at_the_hub = True
    truck_3_at_the_hub = True

    truck_1_delivered = False
    truck_2_delivered = False
    truck_3_delivered = False

    print_1 = False
    print_2 = False
    print_3 = False

    while truck_1_delivered is False or truck_2_delivered is False or truck_3_delivered is False:
        print("(1) Search package ID")
        print("(2) Search package address")
        print("(3) search package deadline")
        print("(4) Search package city")
        print("(5) Search package zip_code")
        print("(6) Search package weight")
        print("(7) Search package status")
        search_number = input("Please enter the search number (enter 0 to skip): ")

        try:
            if int(search_number) >= 1 and int(search_number) <= 7:
                search_crit = input("Please enter search criterea: ")
                search_main(search_number, search_crit, truck_1, truck_2, truck_3)

            elif int(search_number) == 0:
                print("Search skipped")

            else:
                print("Please enter a value 0-7")

        except:
            print("Please enter a value 0-7")

        # This corrects the address of package 9 after 10:20
        if truck_2_time >= datetime.datetime(2022, 11, 2, 10, 20):
            for i in range(len(truck_2)):
                if truck_2[i]['p_id'] == 9:
                    # 410 S State St., Salt Lake City, UT 84111
                    truck_2[i]['address'] = '410 S State St'
                    truck_2[i]['city'] = 'Salt Lake City'
                    truck_2[i]['zip_c'] = '84111'

        # This starts truck_1 delivery
        if truck_1_delivered is False:

            # Truck_1 as has left the hub
            # This sets all packages to en route
            if truck_1_at_the_hub is True:
                for i in range(len(truck_1)):
                    truck_1[i]['status'] = 'en route'
                truck_1_at_the_hub = False

            # This block calculates time and distance
            package_to_be_delivered = truck_1[truck_1_count]
            truck_1_distance += g.get_distance(first_truck_location, truck_1[truck_1_count]['address'])
            time_to_delivery = str(round(g.get_distance(first_truck_location, truck_1[truck_1_count]['address']) / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_1_time = truck_1_time + tdelta
            first_truck_location = truck_1[truck_1_count]['address']
            truck_1[truck_1_count]['status'] = 'delivered'
            truck_1[truck_1_count]['delivery_time'] = truck_1_time

            truck_1_count += 1

        # This starts truck_2 delivery
        if truck_1_time > datetime.datetime(2022, 11, 2, 9, 5) and truck_2_delivered is False:
            # Truck_2 as has left the hub
            # This sets all packages to en route
            if truck_2_at_the_hub is True:
                for i in range(len(truck_2)):
                    truck_2[i]['status'] = 'en route'
                truck_2_at_the_hub = False

            # This block calculates time and distance
            package_to_be_delivered = truck_2[truck_2_count]
            truck_2_distance += g.get_distance(second_truck_location, truck_2[truck_2_count]['address'])
            time_to_delivery = str(round(g.get_distance(second_truck_location, truck_2[truck_2_count]['address']) / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_2_time = truck_2_time + tdelta
            second_truck_location = truck_2[truck_2_count]['address']
            truck_2[truck_2_count]['status'] = 'delivered'
            truck_2[truck_2_count]['delivery_time'] = truck_2_time

            truck_2_count += 1

        # This starts truck_3 delivery after truck_1 has returned to the hub
        if truck_1_delivered is True:
            # Truck_1 as has left the hub
            # This sets all packages to en route
            if truck_3_at_the_hub is True:
                for i in range(len(truck_3)):
                    truck_3[i]['status'] = 'en route'
                truck_3_at_the_hub = False
                truck_3_time = truck_1_time

            # This block calculates time and distance

            package_to_be_delivered = truck_3[truck_3_count]
            truck_3_distance += g.get_distance(third_truck_location, truck_3[truck_3_count]['address'])
            time_to_delivery = str(round(g.get_distance(third_truck_location, truck_3[truck_3_count]['address']) / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_3_time = truck_3_time + tdelta
            third_truck_location = truck_3[truck_3_count]['address']
            truck_3[truck_3_count]['status'] = 'delivered'
            truck_3[truck_3_count]['delivery_time'] = truck_3_time

            truck_3_count += 1

            #truck_1_time = truck_3_time

            # if truck_2_delivered is True:
            #     truck_2_time = truck_3_time

        # This prints the status of all package between 8:35 and 9:35
        if truck_1_time >= datetime.datetime(2022, 11, 2, 8, 35) and print_1 is False:
            print("Print 1")
            print("truck_1 time: " + str(truck_1_time) + " truck_1_distance: " + str(truck_1_distance))
            print("truck_2_time: " + str(truck_2_time) + " truck_2_distance: " + str(truck_2_distance))
            print("truck_3_time: " + str(truck_3_time) + " truck_3_distance: " + str(truck_3_distance))
            for i in range(len(truck_1)):
                print("Truck_1: " + "Package ID: " + str(truck_1[i]['p_id']) + " Status: " + str(truck_1[i]['status'])
                      + " Delivery Time: " + str(truck_1[i]['delivery_time']))

            for i in range(len(truck_2)):
                print("Truck_2: " + "Package ID: " + str(truck_2[i]['p_id']) + " Status: " + str(truck_2[i]['status'])
                      + " Delivery Time: " + str(truck_2[i]['delivery_time']))

            for i in range(len(truck_3)):
                print("Truck_3: " + "Package ID: " + str(truck_3[i]['p_id']) + " Status: " + str(truck_3[i]['status'])
                      + " Delivery Time: " + str(truck_3[i]['delivery_time']))

            print_1 = True

        # This prints the status of all packages between 9:35 and 10:25
        if truck_2_time >= datetime.datetime(2022, 11, 2, 9, 35) and print_2 is False:
            print("\nPrint 2")
            print("truck_1 time: " + str(truck_1_time) + " truck_1_distance: " + str(truck_1_distance))
            print("truck_2_time: " + str(truck_2_time) + " truck_2_distance: " + str(truck_2_distance))
            print("truck_3_time: " + str(truck_3_time) + " truck_3_distance: " + str(truck_3_distance))

            for i in range(len(truck_1)):
                print("Truck_1: " + "Package ID: " + str(truck_1[i]['p_id']) + " Status: " + str(truck_1[i]['status'])
                      + " Delivery Time: " + str(truck_1[i]['delivery_time']))

            for i in range(len(truck_2)):
                print("Truck_2: " + "Package ID: " + str(truck_2[i]['p_id']) + " Status: " + str(truck_2[i]['status'])
                      + " Delivery Time: " + str(truck_2[i]['delivery_time']))

            for i in range(len(truck_3)):
                print("Truck_3: " + "Package ID: " + str(truck_3[i]['p_id']) + " Status: " + str(truck_3[i]['status'])
                      + " Delivery Time: " + str(truck_3[i]['delivery_time']))

            print_2 = True

        # This prints the status of all package between 12:03 and 1:12
        if truck_3_time >= datetime.datetime(2022, 11, 2, 12, 3) and print_3 is False:
            print("\nPrint 3")
            print("truck_1 time: " + str(truck_1_time) + " truck_1_distance: " + str(truck_1_distance))
            print("truck_2_time: " + str(truck_2_time) + " truck_2_distance: " + str(truck_2_distance))
            print("truck_3_time: " + str(truck_3_time) + " truck_3_distance: " + str(truck_3_distance))

            for i in range(len(truck_1)):
                print("Truck_1: " + "Package ID: " + str(truck_1[i]['p_id']) + " Status: " + str(truck_1[i]['status'])
                      + " Delivery Time: " + str(truck_1[i]['delivery_time']))

            for i in range(len(truck_2)):
                print("Truck_2: " + "Package ID: " + str(truck_2[i]['p_id']) + " Status: " + str(truck_2[i]['status'])
                      + " Delivery Time: " + str(truck_2[i]['delivery_time']))

            for i in range(len(truck_3)):
                print("Truck_3: " + "Package ID: " + str(truck_3[i]['p_id']) + " Status: " + str(truck_3[i]['status'])
                      + " Delivery Time: " + str(truck_3[i]['delivery_time']))

            print_3 = True

        # This returns truck_1 to the hub after all the packages have been delivered
        if truck_1_count == len(truck_1):
            truck_1_delivered = True
            truck_1_distance += g.get_distance(first_truck_location, '4001 South 700 East')
            time_to_delivery = str(round(g.get_distance(first_truck_location, '4001 South 700 East') / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_1_time = truck_1_time + tdelta
            first_truck_location = '4001 South 700 East'

        # This returns truck_2 to the hub after all the packages have been delivered
        if truck_2_count == len(truck_2):
            truck_2_delivered = True
            truck_2_distance += g.get_distance(second_truck_location, '4001 South 700 East')
            time_to_delivery = str(round(g.get_distance(second_truck_location, '4001 South 700 East') / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_2_time = truck_2_time + tdelta
            second_truck_location = '4001 South 700 East'

        # This returns truck_3 to the hub after all the packages have been delivered
        if truck_3_count == len(truck_3):
            truck_3_delivered = True
            truck_3_distance += g.get_distance(third_truck_location, '4001 South 700 East')
            time_to_delivery = str(round(g.get_distance(third_truck_location, '4001 South 700 East') / .3, 2))
            frmt = time_to_delivery.split('.')

            tdelta = datetime.timedelta(minutes=float(frmt[0]), seconds=float(frmt[1]))
            truck_3_time = truck_3_time + tdelta
            third_truck_location = '4001 South 700 East'

            # truck_1_time = truck_3_time

            # if truck_2_delivered is True:
            #     truck_2_time = truck_3_time

    print("End of Program")