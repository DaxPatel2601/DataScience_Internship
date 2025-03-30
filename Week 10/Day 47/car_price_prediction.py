import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score

# le = LabelEncoder()
#
# df=pd.read_csv("cardekho_dataset.csv")
#
# df[["brand","model","seller_type","fuel_type","transmission_type"]]=df[["brand","model","seller_type","fuel_type","transmission_type"]].apply(le.fit_transform)
#
# # print(df)
# # print(df.isnull().sum())
# df.to_csv("encoded_cardekho.csv")

df2=pd.read_csv("encoded_cardekho.csv")

x = df2[["brand","model","vehicle_age","km_driven","seller_type","fuel_type","transmission_type","mileage","engine","max_power","seats"]]
y = df2[["selling_price"]]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

brand = input("Enter Brand (numeric code): ")
model = input("Enter Model (numeric code): ")
vehicle_age = float(input("Enter Vehicle Age (years): "))
km_driven = float(input("Enter Kilometers Driven: "))
seller_type = input("Enter Seller Type (numeric code): ")
fuel_type = input("Enter Fuel Type (numeric code): ")
transmission_type = input("Enter Transmission Type (numeric code): ")
mileage = float(input("Enter Mileage (km/l): "))
engine = float(input("Enter Engine Capacity (cc): "))
max_power = float(input("Enter Max Power (bhp): "))
seats = int(input("Enter Number of Seats: "))

user_data = pd.DataFrame([[brand, model, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats]],
                         columns=x.columns)

predicted_price = rf.predict(user_data)

print(f"\n🚗 Estimated Selling Price: ₹{predicted_price[0]:,.2f}")

# coustom=rf.predict([])


# st.write(f"Accuracy: {accuracy:.2f}")