import pandas as pd

#CARGANDO LOS 5 ARCHIVOS CSV EN DATAFRAMES DE PANDAS
df_customers = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_customers_dataset.csv')
df_order_items = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_order_items_dataset.csv')
df_order_payments = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_order_payments_dataset.csv')
df_orders = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_orders_dataset.csv')
df_products = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_products_dataset.csv')

#ESTABLECIENDO LAS PK EN EL DATAFRAME
df_customers.set_index('customer_id', inplace=True)
df_order_items.set_index('order_id', inplace=True)
df_order_payments.set_index('order_id', inplace=True)
df_orders.set_index('order_id', inplace=True)
df_products.set_index('product_id', inplace=True)