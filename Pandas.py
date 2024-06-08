import pandas as pd

#CARGANDO LOS 5 ARCHIVOS CSV EN DATAFRAMES DE PANDAS
df_customers = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_customers_dataset.csv')
df_order_items = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_order_items_dataset.csv')
df_order_payments = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_order_payments_dataset.csv')
df_orders = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_orders_dataset.csv')
df_products = pd.read_csv('U:/CAVILES/CAPACITACION/2024/DATA_ENGINEER/TP1-Parte3/ecommerce_products_dataset.csv')

