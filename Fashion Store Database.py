#Fashion Store Database
import mysql.connector

mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='VANYA',
                             database='fashion')
mycursor=mydb.cursor()

def AddProduct():
    L=[]
    stk=[]
    pid=input("Enter the Product ID: ")
    L.append(pid)
    IName=input("Enter the Product Name:")

    L.append(IName)
    brnd=input("Enter the Product Brand Name: ")
    L.append(brnd)
    fr=input("Enter Male/Female/Kids: ")
    L.append(fr)
    sn=input("Enter Winter/Summer: ")
    L.append(sn)
    rate=int(input("Enter the Rates for Product :"))
    L.append(rate)
    product=(L)
    sql="Insert into product(product_id,PName,brand,Product_for,Season,rate)values(%s, %s, %s, %s,%s,%s)"
    mycursor.execute(sql,product)
    mydb.commit()
    print('One Product inserted')
    instk=int(input('Enter number of items available :'))
    h='NO'
    mycursor.execute("Insert into stock(item_id, Instock, status) values('{}', {}, '{}')".format(pid, instk, h))
    mydb.commit()
    
def ViewProduct():
    sql='select * from Product'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)

def EditProduct():
    pid=input('Enter product ID to be edited:')
    sql='select * from product where product_id=%s'
    ed=(pid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    print("")
    s=input('Enter what you want to edit(product_for/ season/ rate) :')

    if s=='rate': 
        #fld=input("Enter the field which you want to edit :")
        val=int(input("Enter the rate value you want to set: "))
        mycursor.execute("Update product set rate ={} where product_id='{}'".format(val,pid))
        mydb.commit()
        print("Editing Done")
        print("After correction the record is: ")
        sql="select * from product"
        #ed=(pid,)
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print(x)

    elif s=='season':
        seas=input('Enter new season you want to set(W/ S/ Both) :')
        mycursor.execute("Update product set season= '{}' where product_id= '{}'".format(seas,pid))
        mydb.commit()
        print("Editing Done")
        print("After correction the record is: ")
        sql="select * from product"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print(x)

    elif s=='product_for':
        seas=input('Enter new product for you want to set(M/ F/ K/ All) :')
        mycursor.execute("Update product set product_for = '{}' where product_id= '{}'".format(seas ,pid))
        mydb.commit()
        print("Editing Done")
        print("After correction the record is: ")
        sql="select * from product"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print(x)
                
        
def DelProduct():
    pid=input('Enter the Product id to be deleted:')
    
    mycursor.execute("delete from product where product_id='{}'".format(pid))
    mydb.commit()
    print('One Item Deleted')
    sql='select * from Product'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)
    mycursor.execute("delete from stock where item_id='{}'".format(pid))
    mydb.commit()
    
def PurchaseProduct():
    h=0
    L=[]
    pid=input("Enter the Purchase ID: ")
    L.append(pid)
    prid=input("Enter the Product ID:")
    L.append(prid)
    sql='select * from product where product_id=%s'
    ed=(prid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    h=res[0][5]    
    for x in res:
        print(x)
    brnd=int(input("Enter the No of items : "))
    L.append(brnd)
    rate= h*brnd
    L.append(rate)
    product=(L)
    mycursor.execute("Insert into purchase(purchase_id, item_id, no_of_items, amount) values('{}', '{}', {}, {})".format(pid, prid, brnd, int(rate)))
    mydb.commit()
    print('Item Purchased')
    sql='select * from Purchase'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)
    sql='select * from stock where item_id=%s'
    ed=(prid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    m=res[0][1]
    up=m-brnd
    mycursor.execute("Update stock set Instock={} where item_id='{}'".format(up, prid))
    mydb.commit()
    
    
def ViewPurchase():
    sql="select Pname from product"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    item=input('Enter Product Name:')
    mycursor.execute("select product.product_id, product.Pname, product.brand, purchase.no_of_items, purchase.amount from product, purchase where product.product_id= purchase.item_id and product.PName='{}'".format(item))
    res=mycursor.fetchall()
    for x in res:
        print(x)

def ViewStock():
    sql='select Pname from Product'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)
    item=input('Enter product name:')
    sql='select product.product_id, product.Pname, stock.Instock from stock, product where product.product_id=stock.item_id and product.Pname=%s'
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    for x in res:
        print(x)

def SaleProduct():
    L=[]
    sid=input("Enter the Sale ID: ")
    prid=input("Enter the Product ID:")
    sql='select * from product where product_id=%s'
    ed=(prid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    brnd=int(input("Enter the No of items sold : "))
    rate=int(input("Enter the new selling price per item after sale :"))
    amnt= rate * brnd
    mycursor.execute("Insert into sales(sale_id, item_id, no_of_item_sold, sale_rate, amount) values('{}', '{}', {}, {}, {})".format(sid, prid, brnd, rate, amnt))
    mydb.commit()
    print('Item Sold')
    sql='select * from Sales'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)
    sql='select * from stock where item_id=%s'
    ed=(prid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    m=res[0][1]
    up=m-brnd
    mycursor.execute("Update stock set Instock={} where item_id='{}'".format(up, prid))
    mydb.commit()

def ViewSales():
    sql='select Pname from Product'
    mycursor.execute(sql)
    res= mycursor.fetchall()
    for x in res:
        print(x)
    item=input('Enter Product Name:')
    mycursor.execute("select product.product_id, product.PName, product.brand, sales.no_of_item_sold, sales.amount from sales, product where product.product_id=sales.item_id and product.PName='{}'".format(item))
    res=mycursor.fetchall()
    for x in res:
        print(x)

def MenuSet(): #Function For The Fashion Store System
    while True:

        print()
        print()
        print('Enter 1: To Add Product')
        print('Enter 2: To View Product')
        print('Enter 3: To Edit Product')
        print('Enter 4: To Delete Product')
        print('Enter 5: To Purchase Product')
        print('Enter 6: To View Purchases')
        print('Enter 7: To Sale the item')
        print('Enter 8: To View Sales Details')
        print('Enter 9: To View Stock')
        print('Enter 10: Break')
        print()
        print()
        
        userinput=int(input('Please select an above option:')) #Will Take Input From User
        if(userinput == 1):
            AddProduct()

        elif (userinput == 2):
            ViewProduct()

        elif(userinput == 3):
            EditProduct()

        elif (userinput==4):
            DelProduct()
            
        elif (userinput==5):
            PurchaseProduct()

        elif (userinput==6):
            ViewPurchase()


        elif (userinput==7):
            SaleProduct()

        elif (userinput==8):
            ViewSales()

        elif (userinput==9):
            ViewStock()
            
        elif userinput==10:
            break

        else:
            print("Enter correct choice...")
MenuSet()
