#tower of hanoi- recursion

def tower_of_hanoi_recursive(n, source, auxiliary, target):
    # Base case: If there's only one disk, move it directly from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary using target as the temporary storage
    tower_of_hanoi_recursive(n - 1, source, target, auxiliary)

    # Move the remaining disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n-1 disks from auxiliary to target using source as the temporary storage
    tower_of_hanoi_recursive(n - 1, auxiliary, source, target)

# Example usage:
num_disks = 3
tower_of_hanoi_recursive(num_disks, 'A', 'B', 'C')
