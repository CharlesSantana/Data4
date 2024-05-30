import pandas
import pandas as pd

# Leitura do arquivo de clientes
clientes_df = pd.read_csv('/home/master/dados/datasets/olist_customers_dataset.csv')

# Leitura do arquivo de geolocalizacao
localizacao_df = pd.read_csv('/home/master/dados/datasets/olist_order_payments_dataset.csv')

# Leitura do arquivo de pedidos
pedidos_df = pd.read_csv('/home/master/dados/datasets/olist_orders_dataset.csv')

# Leitura do arquivo de itens do pedido
itens_df = pd.read_csv('/home/master/dados/datasets/olist_order_items_dataset.csv')

# Leitura do arquivo de pagamentos
pagamentos_df = pd.read_csv('/home/master/dados/datasets/olist_order_payments_dataset.csv')

# Leitura do arquivo de comentarios
comentarios_df = pd.read_csv('/home/master/dados/datasets/olist_order_reviews_dataset.csv')

# Leitura do arquivo de produtos
produtos_df = pd.read_csv('/home/master/dados/datasets/olist_products_dataset.csv')

# Leitura do arquivo de vendas
vendas_df = pd.read_csv('/home/master/dados/datasets/olist_sellers_dataset.csv')

# Leitura do arquivo de nometransacao
trasacao_df = pd.read_csv('/home/master/dados/datasets/product_category_name_translation.csv')

#Unir datasets

df_geral = pd.merge(pedidos_df, pagamentos_df, on='order_id').merge(itens_df, on='order_id').merge(clientes_df,on='customer_id').merge(produtos_df, on='product_id').merge(vendas_df, on='seller_id')


df_geral.to_csv('/home/master/dados/datasets/dataset_olist.csv', index=False)
