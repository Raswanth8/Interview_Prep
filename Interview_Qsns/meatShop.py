"""
Program Details
 A pizza shop makes vegan pizzas as well as meat based pizzas. The customers place N orders at the shop and their order number gets printed on thier bill.
 The shop displays K out of N both - vegan and meat based pizza orders on thier display screen at a single time.The pizza shop is very famous and receives many orders. 
 So to avoid confusion, the vegan pizza orders are displayed as a positive order number and the meat based pizza orders are displayed as a negative order number.
 All the orders are delivered in the order in which they are displayed on the screen.Each time a displayed order is ready, it is then removed from the display screen and 
 the next order is added to the display at the end.
 
 A couple has come to eat pizza with their child Billy. Billy is a very naughty child and to keep him busy, 
 his parents tell him to make a list of the first meat nased pizza order number present in each set of K orders displayed on the shop's display scrren.
 
 Write an algorithm to help Billy make a list of the first meat based pizza order numbers displayed on the screen each time an order is delivered to a customer.
 
 Input:
 The first line of the input consists of two space-separated integers - numofOrders and size, representing the total number of orders placed (N) and the number
 of orders displayed on the screen (K), respectively.
 The second line consists of N space-separated integers representing the vegan pizza and meat based pizza order numbers of the orders placed by the customers.
 
 Output:
 Print a list of space-separated integers representing the first meat based pizza order of every K orders displayed on the screen each time an order is
 delivered to a customer and print 0 it the screen does not display any meat based pizza order.
 
 Constraints:
 0 <= numofOrders <= 10^6
 0 <= size <= numofOrders
 -10^9 <= ordersNum <= 10^9; where orderNum represents the order numbers of the orders placed.
 
 Example:
 Input:
 6,3
 -11 -2 19 37 64 -18
 Output:
 -11 -2 0 -18

"""


def func(nums, k):
    res = []
    n = len(nums)
    for i in range(n-k+1):
        found = 0
        for j in range(i, i+k):
            if nums[j] < 0:
                res.append(nums[j])
                found = 1
                break
        if found == 0:
            res.append(0)
    return res


print(func([-11, -2, 19, 37, 64, -18], 3))
