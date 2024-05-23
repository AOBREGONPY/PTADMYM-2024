def calculate_discount(row):
    try:
        base_price = float(''.join(filter(str.isdigit, row['PRECIO_BASE'].replace(',', '').replace('.', ''))))
        discount_price = float(''.join(filter(str.isdigit, row['PRECIO_CON_DESCUENTO'].replace(',', '').replace('.', ''))))
        if base_price == discount_price:
            return 'No tiene descuento'
        else:
            discount_percentage = ((base_price - discount_price) / base_price) * 100
            return f"{discount_percentage:.2f}%"
    except ValueError:
        return 'N/A'
