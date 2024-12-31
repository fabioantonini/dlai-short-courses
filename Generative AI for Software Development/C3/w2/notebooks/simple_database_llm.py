from sqlalchemy import create_engine, text

# Create the engine
engine = create_engine('sqlite:///ecommerce.db', echo=True)

# Check the connection
try:
    # Establish a connection
    with engine.connect() as connection:
        # Execute a simple query
        result = connection.execute(text("SELECT 1"))
        
        # Fetch the result
        output = result.fetchone()
        
        # Print the output
        print("Connection is live. Query result:", output)
except Exception as e:
    print("An error occurred:", e)