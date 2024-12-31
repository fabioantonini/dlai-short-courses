from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, ForeignKey, insert, select
import os

# Delete the existing database file
if os.path.exists('ecommerce.db'):
    os.remove('ecommerce.db')

engine = create_engine('sqlite:///ecommerce.db', echo=True)  # Enable echo for SQL logging

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('email', String, unique=True))

products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('price', Integer))

orders = Table('orders', metadata,
               Column('id', Integer, primary_key=True),
               Column('user_id', Integer, ForeignKey('users.id')))

order_items = Table('order_items', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('order_id', Integer, ForeignKey('orders.id')),
                    Column('product_id', Integer, ForeignKey('products.id')),
                    Column('quantity', Integer))

# Create all tables
metadata.create_all(engine)
print("Tables created.")

def add_user(engine, name, email):
    # Create a connection to the database
    with engine.connect() as connection:
         # Begin a transaction
        trans = connection.begin()
        # Prepare the insert statement
        stmt = users.insert().values(name=name, email=email)
        print(f"Executing: {stmt}")
        # Execute the statement
        try:
            # Execute the statement
            connection.execute(stmt)

            # Commit the transaction
            trans.commit()
            print(f"User '{name}' added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
add_user(engine, 'Alice Johnson', 'alice.johnson@example.com')
add_user(engine, 'John Doo', 'john.doo@example.com')
add_user(engine, 'Pippo Baudo', 'pippo.baudo@example.com')


with engine.connect() as connection:
    result = connection.execute(select(users))
    for row in result:
        print(row)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users"))
    for row in result:
        print(row)

def get_all_users(engine):
    # Create a connection to the database
    with engine.connect() as connection:
        # Prepare the select statement
        stmt = select(users)
        
        # Execute the statement and fetch all results
        result = connection.execute(stmt)
        users_list = result.fetchall()
        
        # Check if any users were found
        if not users_list:
            print("No users found in the database.")
        
        # Return the list of users
        return users_list

# Example usage
all_users = get_all_users(engine)
for user in all_users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")


from sqlalchemy import update

def update_user_email(engine, user_id, new_email):
    # Create a connection to the database
    with engine.connect() as connection:
        # Begin a transaction
        trans = connection.begin()
        try:
            # Prepare the update statement
            stmt = (
                update(users)
                .where(users.c.id == user_id)
                .values(email=new_email)
            )
            print(f"Executing: {stmt}")

            # Execute the statement
            result = connection.execute(stmt)

            # Check if any row was updated
            if result.rowcount > 0:
                # Commit the transaction
                trans.commit()
                print(f"User ID {user_id}'s email updated to '{new_email}'.")
            else:
                # Rollback if no rows were updated
                trans.rollback()
                print(f"No user found with ID {user_id}.")
        except Exception as e:
            # Rollback in case of error
            trans.rollback()
            print(f"An error occurred: {e}")

# Example usage
update_user_email(engine, 1, 'new.alice@example.com')

# Verify the update
all_users = get_all_users(engine)
for user in all_users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")


from sqlalchemy import delete

def delete_user(engine, user_id):
    # Create a connection to the database
    with engine.connect() as connection:
        # Begin a transaction
        trans = connection.begin()
        try:
            # Prepare the delete statement
            stmt = delete(users).where(users.c.id == user_id)
            print(f"Executing: {stmt}")

            # Execute the statement
            result = connection.execute(stmt)

            # Check if any row was deleted
            if result.rowcount > 0:
                # Commit the transaction
                trans.commit()
                print(f"User ID {user_id} deleted successfully.")
            else:
                # Rollback if no rows were deleted
                trans.rollback()
                print(f"No user found with ID {user_id}.")
        except Exception as e:
            # Rollback in case of error
            trans.rollback()
            print(f"An error occurred: {e}")

# Example usage
delete_user(engine, 1)

# Verify the deletion
all_users = get_all_users(engine)
for user in all_users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
