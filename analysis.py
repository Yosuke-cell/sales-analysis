# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd

def main():
    try:
        df = pd.read_csv("sales.csv", encoding="utf-8")
        df["TotalSales"] = df["Quantity"] * df["Price"]
        total_sales = df["TotalSales"].sum()
        sales_by_category = df.groupby("Category")["TotalSales"].sum()
        product_sales = df.groupby("Product")["TotalSales"].sum()
        top_product = product_sales.idxmax()
        top_product_value = product_sales.max()
        region_sales = df.groupby("Region")["TotalSales"].sum()
        high_value_orders = df[df["TotalSales"] > 200]
        print("\n===== TOTAL SALES =====")
        print(f"${total_sales:.2f}")
        print("\n===== SALES BY CATEGORY =====")
        print(sales_by_category)
        print("\n===== TOP-SELLING PRODUCT =====")
        print(f"{top_product} (${top_product_value:.2f})")
        print("\n===== REGION-WISE SALES =====")
        print(region_sales)
        print("\n===== ORDERS WITH SALES > $200 =====")
        print(high_value_orders)
        print("\n=== Analysis Completed Successfully ===")
    except FileNotFoundError:
        print("Error: sales.csv file not found. Make sure it is in the same folder.")
    except Exception as e:
        print("An unexpected error occurred:", e)
if __name__ == "__main__":
    main()