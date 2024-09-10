CREATE TABLE user_table ( 
    user_id SERIAL PRIMARY KEY, 
    first_name VARCHAR(25) NOT NULL, 
    last_name VARCHAR(25) NOT NULL,
    password VARCHAR(16) NOT NULL, 
    email VARCHAR(254) UNIQUE NOT NULL, 
    phone_number VARCHAR(15), 
    role VARCHAR(20), 
    profile_image VARCHAR 
 );
   
  
CREATE TABLE land_buyer (
    buyer_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user_table (user_id),
    lawyer_id INTEGER REFERENCES lawyer (lawyer_id),
    address VARCHAR(30)
);

CREATE TABLE land_seller (
    seller_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user_table (user_id),
    lawyer_id INTEGER REFERENCES lawyer (lawyer_id),
    address VARCHAR(25)
);

CREATE TABLE lawyer (
    lawyer_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user_table (user_id),
    firm VARCHAR(25),
    profile_image VARCHAR
);

CREATE TABLE land_details_table (
    land_details_id SERIAL PRIMARY KEY,
    seller_id INTEGER REFERENCES land_seller (seller_id),
    buyer_id INTEGER REFERENCES land_buyer (buyer_id),
    parcel_number FLOAT,
    property_address VARCHAR(30),
    date_acquired DATE,
    date_of_issue DATE,
    owner_name VARCHAR(25),
    land_history JSONB
);

CREATE TABLE drafted_smart_contract (
    drafted_contract_id SERIAL PRIMARY KEY,
    seller_id INTEGER REFERENCES land_seller (seller_id),
    buyer_id INTEGER REFERENCES land_buyer (buyer_id),
    lawyer_id INTEGER REFERENCES lawyer (lawyer_id),
    date_created DATE,
    contract_duration INTEGER,
    agreed_amount INTEGER,
    installment_schedule INTEGER,
    penalties_interest_rate INTEGER,
    down_payment INTEGER
);

CREATE TABLE chatroom (
    chat_id SERIAL PRIMARY KEY,
    message TEXT,
    lawyer_id INTEGER REFERENCES lawyer (lawyer_id),
    seller_id INTEGER REFERENCES land_seller (seller_id),
    buyer_id INTEGER REFERENCES land_buyer (buyer_id),
    time_sent TIMESTAMP,
    receiver VARCHAR(25),
    sender VARCHAR(25)
);