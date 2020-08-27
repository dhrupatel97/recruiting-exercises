import unittest
from inventory_allocation import InvertoryAllocation

class TestInventoryAllocation(unittest.TestCase):

    def test_happy_case(self) -> None:
        """testing a simple/happy case
        """

        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)
    
    def test_not_enough_inventory(self) -> None:
        """testing for Not enough inventory
        """

        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)

    def test_no_order(self) -> None:
        """testing for no order
        """

        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)

    def test_no_inventory(self) -> None:
        """testing for No inventory
        """

        order = {'apple': 3}
        inventory = []
        output = []

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven) 
        
    def test_split(self) -> None:
        """testing for spliting an item order across warehouses 
           if that is the only way to completely ship an item
        """

        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [ {'owd': {'apple': 5}}, {'dm': {'apple': 5}}]

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)
    
    def test_new_item(self) -> None:
        """testing an item which is not present in inventory
        """

        order = {'apple': 10, 'orange': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)
    
    def test_multiple_orders(self):
        """testing for multiple order across the inventories
        """
        
        order = {'apple': 20, 'dragonfruit': 7, 'peach': 68}
        inventory = [{'name': 'owd', 'inventory': {'apple': 15, 'dragonfruit': 12}}, {'name': 'dm', 'inventory': {'apple': 25}}]
        output = [{'owd': {'apple': 15, 'dragonfruit': 7}}, {'dm': {'apple': 5}}]

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)

    def test_zero_order_value(self):
        """testing for an order with value zero
        """
        
        order = {'apple': 0, 'dragonfruit': 7, 'peach': 68}
        inventory = [{'name': 'owd', 'inventory': {'apple': 15, 'dragonfruit': 12}}, {'name': 'dm', 'inventory': {'apple': 25}}]
        output = [{'owd': {'dragonfruit': 7}}]

        inven = InvertoryAllocation().shipment(order, inventory)
        self.assertEqual(output, inven)
if __name__ == "__main__":
    unittest.main(verbosity=2)