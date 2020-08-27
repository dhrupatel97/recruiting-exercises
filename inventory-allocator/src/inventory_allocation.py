from typing import Dict, List, Any
import copy

# Created by Dhruv Patel

class InvertoryAllocation:
    """Implementated an InventoryAllocator class to produce the cheapest shipment
       and compute a best way an order can be shipped given inventory across a set if warehouse
    """
    
    def shipment(self, order: Dict[str, int], inventory: List[dict]) -> List[dict]:
        """Completes the required order according to the availability of product
           and updates the inventory according
        """
        
        output = dict()

        # check if there are orders available or has inventories
        if len(order) == 0 or len(inventory) == 0:
            return list(output)
        
        temp_new_inventory = list()

        # copying the original inventory
        temp_inventory: list = copy.deepcopy(inventory)

        for fruit, value in order.items():

            # if the order value is zero
            if value > 0:
                my_order_value: int = value

                for x in range(len(temp_inventory)):

                    if fruit not in temp_inventory[x]['inventory']:
                        break
                    
                    if temp_inventory[x]['inventory'][fruit] == 0:
                        break
                    
                    key, order_left, temp_new_inventory, output= self.inventory_update(fruit, my_order_value, temp_inventory[x], output)

                    my_order_value = order_left

                    if order_left != 0:
                        continue
                    else:
                        break      

        # creating a list of dictionary for output
        result = list()

        for k, v in output.items():
            temp = dict()
            temp[k] = v
            result.append(temp)
            del temp

        return result


    def inventory_update(self, key: str, required: int, temp_inventory: Dict[str, int], output: dict):
        """Updates the inventory when the product is taken 
        and return a new inventory along with the order left
        """
        
        name: str = temp_inventory['name']
        item: Dict[str, int] = temp_inventory['inventory']

        old_inventory: Dict[str, int] = copy.deepcopy(temp_inventory)
        
        # if stock value is more
        if item[key] > required:
            total_stock: int = item[key]
            item[key] = item[key] - required
            
            total_used: int = total_stock - item[key]
            require_left: int = required - total_used

            t_u = old_inventory['inventory']
            t_u[key] = total_used

            if name not in output:
                output.update({name: {key: t_u[key]}})
            else:
                output[name][key] = t_u[key]

        # if stock value is less
        else:
            require_left: int = required - item[key]
            item[key]  = 0
            
            p = old_inventory['inventory']
            output[name] = p

        return (key, require_left, temp_inventory, output)


