from werkzeug.security import generate_password_hash, check_password_hash


class Products:
    """Functionality of products"""

    products = {}

    def get_all_products(self):
        """"
        get all products
        """
        if self.products == {}:
            return {"txt": "Product not found"}
        return self.products

    def get_a_product(self, product_id):
        if self.products == {}:
            return {"txt": "Product not found"}
        return self.products[product_id]

    def create_product(self, product_name, product_price):
        new_id = len(self.products) + 1
        self.products[new_id] = {"product_name": product_name,
                                 "product_price": product_price, }
        res = self.products[new_id]
        return {"msg": "Product added successfully", "data": res}

    def edit_product(self, product_id, product_name, product_price):
        self.products[product_id] = {"product_id": product_id, "product_name": product_name,
                                     "product_price": product_price}
        return {"msg": "Sale Edited"}

    def delete_a_product(self, product_id):
        if product_id not in self.products:
            return {"txt": "product not found"}
        del self.products[product_id]
        return {"txt": "product Deleted"}


# product = Products()


# print(product.get_all_products())
# print(product.get_a_product(2))
# product.create_product("Socks", 456)
# print(product.products)


class Sales:
    """Functionality of sales"""
    sales = {}

    def see_sales(self):
        if self.sales == {}:
            return {"txt": "No sales added."}
        return self.sales

    def get_a_sale(self, sale_id):
        if self.sales == {} or sale_id not in self.sales:
            return {"txt": "Sale not found."}
        return self.sales[sale_id]

    def post_a_sale(self, product_name, number, sell_price):
        new_id = len(self.sales) + 1
        self.sales[new_id] = {"product_name": product_name, "number": number,
                              "sell_price": sell_price}
        return {"msg": "added successfully"}

    def edit_sale(self, sale_id, product_name, number, sell_price):
        if self.sales == {} or sale_id not in self.sales:
            return {"txt": "Sale not found."}
        self.sales[sale_id] = {"product_name": product_name, "number": number, "sell_price": sell_price}
        return {"msg": "Sale Edited"}

    def delete_a_sale(self, sale_id):
        if sale_id not in self.sales:
            return {"txt": "sale not found"}
        del self.sales[sale_id]
        return {"txt": "sale Deleted"}


# sales_s = Sales()


# print(sales_s.see_sales())
# print(sales_s.get_a_sale(2))
# sales_s.post_a_sale("Bryan", 456, 5000)
# print(sales_s.sales)
# print(sales_s.get_a_sale(1))


class Users:
    users = {"kratos": {"email": "kratso@something.com", "password": generate_password_hash("olympus"), "admin": True}}

    def register_user(self, user_name, email, password):
        hidden = generate_password_hash(password=password)
        self.users[user_name] = {"email": email, "password": hidden}
        res = self.users[user_name]
        return {"msg": "user added successfully", "data": res}

    def login(self, user_name, password):
        if user_name in self.users:
            if check_password_hash(self.users[user_name]["password"], password=password):
                print("Logged In")
                return {"txt": "Successfully logged In"}
            else:
                print("Invalid Password")
                return {"txt": "Invalid Password"}
        else:
            print("Invalid Username")
            return {"txt": "Invalid Username"}

    def get_users(self):
        if self.users == {}:
            return {"txt": "No sales added."}
        return self.users

    def delete_a_user(self, user_name):
        del self.users[user_name]
        return {"txt": "user Deleted"}


# user = Users()
# user.register_user("athena", "athena@something.com", "olympus")
# user.login("kratos", "olympus")
# print(user.users)
