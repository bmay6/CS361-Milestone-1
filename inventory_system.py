class InventorySystem:
    """A simple inventory management system."""
    
    def __init__(self):
        """Initialize an empty inventory dictionary."""
        self.inventory = {}
    
    def add_item(self, item_name, quantity, price=0.0):
        """
        Add a new inventory item.
        
        Args:
            item_name (str): Name of the item
            quantity (int): Quantity of the item
            price (float): Price of the item (optional)
        """
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists. Use 'Update Item Quantity' to modify it.")
        else:
            self.inventory[item_name] = {
                'quantity': quantity,
                'price': price
            }
            print(f"✓ Added '{item_name}' with quantity {quantity}")
    
    def update_quantity(self, item_name, new_quantity):
        """
        Update the quantity of an existing inventory item.
        
        Args:
            item_name (str): Name of the item to update
            new_quantity (int): New quantity value
        """
        if item_name not in self.inventory:
            print(f"✗ Item '{item_name}' not found in inventory.")
        else:
            old_quantity = self.inventory[item_name]['quantity']
            self.inventory[item_name]['quantity'] = new_quantity
            print(f"✓ Updated '{item_name}' quantity from {old_quantity} to {new_quantity}")
    
    def view_inventory(self):
        """Display all items currently in the inventory."""
        if not self.inventory:
            print("✗ Inventory is empty.")
        else:
            print("\n" + "="*60)
            print("CURRENT INVENTORY")
            print("="*60)
            print(f"{'Item Name':<20} {'Quantity':<15} {'Price':<15}")
            print("-"*60)
            for item_name, details in self.inventory.items():
                quantity = details['quantity']
                price = details['price']
                print(f"{item_name:<20} {quantity:<15} ${price:<14.2f}")
            print("="*60 + "\n")


def main():
    """Main function to run the inventory management system."""
    system = InventorySystem()
    
    while True:
        print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add New Inventory Item")
        print("2. Update Item Quantity")
        print("3. View Current Inventory")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add New Inventory Item
            item_name = input("Enter item name: ").strip()
            try:
                quantity = int(input("Enter quantity: ").strip())
                price = float(input("Enter price (optional, press Enter for 0): ").strip() or 0)
                system.add_item(item_name, quantity, price)
            except ValueError:
                print("✗ Invalid input. Please enter valid numbers for quantity and price.")
        
        elif choice == '2':
            # Update Item Quantity
            item_name = input("Enter item name to update: ").strip()
            try:
                new_quantity = int(input("Enter new quantity: ").strip())
                system.update_quantity(item_name, new_quantity)
            except ValueError:
                print("✗ Invalid input. Please enter a valid number for quantity.")
        
        elif choice == '3':
            # View Current Inventory
            system.view_inventory()
        
        elif choice == '4':
            # Exit
            print("Exiting... Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
