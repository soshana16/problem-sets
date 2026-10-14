def main():
    fruit_pricing()
    blue()
    blastoff()
    candy_shop()

def blue():
    red = 3
    purple = red*12
    print(purple)

def blastoff():
    count = int(input("Enter a number: "))
    for i in range(count, 0, -1):
        print (i)
        print ("blastoff!")

def candy_shop():
    candies = ["m&m", "milkyway", "hershey"]
    candies.append("kitkat")
    candies.insert(1, "starburts")
    candies.sort()
    candies.remove("kitkat")
    print(candies)
    user_candies = []
    for i in range (3):
        user_candies.append(input("Favorite 3 candies"))
    all_candies = candies + user_candies
    print(len(all_candies))
    
    for candy in all_candies:
        print(candy)
    total_cost = len(all_candies) * 1.25
    return total_cost

def fruit_pricing():
    fruits = {"apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
    fruits["pear"] = 1.15
    print(fruits.get("peach"))

    for fruit in fruits:
        if fruits[fruit]>= 1.25:
            print(fruit)
    total_cost = (3*fruits["apple"] + 2*fruits["banana"] + 1*fruits["coconut"])
    print(total_cost)
        

if __name__ == "__main__":
    main()
