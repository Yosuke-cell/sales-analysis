# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd

def main():
    try:
        # Read CSV file
        df = pd.read_csv("sales.csv", encoding="utf-8")

        # Calculate total sales for each order
        df["TotalSales"] = df["Quantity"] * df["Price"]

        # 1. Total sales
        total_sales = df["TotalSales"].sum()

        # 2. Total sales by category
        sales_by_category = df.groupby("Category")["TotalSales"].sum()

        # 3. Top-selling product
        product_sales = df.groupby("Product")["TotalSales"].sum()
        top_product = product_sales.idxmax()
        top_product_value = product_sales.max()

        # 4. Region-wise sales distribution
        region_sales = df.groupby("Region")["TotalSales"].sum()

        # 5. Orders where sales > $200
        high_value_orders = df[df["TotalSales"] > 200]

        # Output formatting
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

    except FileNotFoundError:
        print("Error: sales.csv file not found. Make sure it is in the same folder.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()