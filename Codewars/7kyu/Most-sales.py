"""
Description:
You work in the best consumer electronics corporation, 
and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:

    products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
    amounts: [3, 24, 8]
    prices: [199, 299, 399]

    Return the three product names with the highest revenues (amount * price), in descending order (highest to lowest revenue).

Note: if multiple products have the same revenue, order them according to their original positions in the input list.

"""

def top3(products, amounts, prices):
    products_revenues = {}
    for i in range(len(products)):
        products_revenues[products[i]] = amounts[i] * prices[i]
    
    top_three_product_revenue = sorted(products_revenues.values(), reverse=True)[:3]
    result = [None] * 3
    
    for key in products_revenues:
        if products_revenues[key] in top_three_product_revenue:
            revenue_index = top_three_product_revenue.index(products_revenues[key])
            top_three_product_revenue[revenue_index] = None
            result[revenue_index] = key
    return result
        