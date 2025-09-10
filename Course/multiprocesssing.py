from multiprocessing import Process
import time

def brew_coffee(name):
    for i in range(1, 4):
        print(f"Brewing coffee {i} for {name}")
        time.sleep(1)
        print(f"Finished coffee {i} for {name}")

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_coffee, args=("Chai",))
        for i in range(3)
    ]
    
    # Start all processes
    for process in chai_maker:
        process.start()

    # Wait for all processes to complete
    for process in chai_maker:
        process.join()
    print("All chai coffees are ready!")


# Sample Output:
#Brewing coffee 1 for Chai
#Brewing coffee 1 for Chai
#Brewing coffee 1 for Chai
#Finished coffee 1 for Chai
#Brewing coffee 2 for Chai
#Finished coffee 1 for Chai
#Brewing coffee 2 for Chai
#Finished coffee 1 for Chai
#Brewing coffee 2 for Chai
#Finished coffee 2 for Chai
#Brewing coffee 3 for Chai
#Finished coffee 2 for Chai
#Brewing coffee 3 for Chai
#Finished coffee 3 for Chai
#Finished coffee 3 for Chai
#Finished coffee 3 for Chai
#All chai coffees are ready!