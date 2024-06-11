#DETERMINANDO LA CATEGORIA DE PRODUCTO MAS VENDIDA
cat_prod_mas_vendida = df_products.groupby(['product_category_name'])['product_category_name'].count()
#IMPRIMIENDO LA CATEGORIA MAS VENDIDA
print(cat_prod_mas_vendida.sort_values(ascending=False).head(1))