import psycopg2

try:
    connection = psycopg2.connect(
		host= "localhost",
        database= "weekend",
        user= "postgres",
        password= "apple_ball",
        port= 5432
    )

    cursor = connection.cursor()

#Creating Tables

    # create_query = '''
    #      CREATE TABLE IF NOT EXISTS users (
    #         id INT PRIMARY KEY NOT NULL,
    #         name VARCHAR(100) ,
    #         dob DATE,
    #         pprofession VARCHAR(100)
    #     )
    #     '''
    # cursor.execute(create_query)
    # connection.commit()
    
    # create_query = '''
    #     CREATE TABLE IF NOT EXISTS address (
    #         id INT PRIMARY KEY NOT NULL,
    #         FOREIGN KEY(user_id) REFRENCES users(id),
    #         permanent_address VARCHAR(100),
    #         temporary_address VARCHAR(100) 
    #     )


    #     '''
    # cursor.execute(create_query)
    # connection.commit()
        
 #Inserting Dummy Queries

    # insert_query = '''
    #     INSERT INTO users Values(1 ,'James','2004-12-22','accountant' )
    #     INSERT INTO users Values(2 ,'Megan','1998-10-12','doctor' )
    #     INSERT INTO users Values(3 ,'Ben','2000-01-03','lawyer' )
    #     INSERT INTO users Values(4 ,'Tim','1995-11-15','professor' )
    #     INSERT INTO users Values(5 ,'John','2005-07-09','civil engineer' )
         

    #     '''
    # cursor.execute(insert_query)
    # connection.commit()

    # insert_query = '''
    #     INSERT INTO address Values(101,1,'london','melbourne' )
    #     INSERT INTO address Values(102,2,'paris','bejing' )
    #     INSERT INTO address Values(103,3,'new york','mumbai' )
    #     INSERT INTO address Values(104,4,'tokyo','venice' ) 
    #     INSERT INTO address Values(105,5,'cape town','new delhi' )
    #     '''
    # cursor.execute(insert_query)
    # connection.commit()

#Fetching data from user

    #  get_users_query = '''
    #     SELECT id.users,profession.users,permanent.address_address
    #     FROM users 
    #     JOIN address 
    #     ON users.id = address.user_id
        
    # '''
    
    # cursor.execute(get_users_query)
    # print(cursor.fetchall())

#Updating Table and adding column gender

    # alter_table_query ='''
    #     ALTER TABLE users
    #         ADD COLUMN gender VARCHAR(10);
    
    
    # '''

    # cursor.execute(alter_table_query)
    # connection.commit()

#Deleting records of age less than 20yrs

    # delete_value_query ='''
    #     DELETE FROM users WHERE dob > '2001-01-01'


    # '''
    # cursor.execute(delete_value_query)
    # connection.commit()


except Exception as e:
    print("An error has occured", e)
    
finally:
    cursor.close()
    connection.close(