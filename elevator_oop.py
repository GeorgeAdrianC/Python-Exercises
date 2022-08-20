class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        """Tells the current floor"""
        return f"Current floor: {self.current}"
    def up(self):
        """Makes the elevator go up one floor."""
        if -1 <=self.current <10:
            self.current = self.current + 1
        else:
            self.current = self.current
        print(self.current)
    def down(self):
        """Makes the elevator go down one floor."""
        if -1<self.current<=10:
            self.current = self.current - 1
        else:
            self.current = self.current
        print(self.current)
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if -1<=floor<=10:
            self.current = floor
        else:
            self.current = self.current
        print(self.current)

        
        

elevator = Elevator(-1, 10, 0)
        

elevator = Elevator(-1, 10, 0)

elevator.up() 
 #should output 1

elevator.down() 
 #should output 0

elevator.go_to(10) 
 #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)