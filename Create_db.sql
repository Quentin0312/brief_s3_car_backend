CREATE TABLE Manufacturer(
   name VARCHAR(50),
   PRIMARY KEY(name)
);

CREATE TABLE Model(
   model VARCHAR(50),
   PRIMARY KEY(model)
);

CREATE TABLE Category(
   name VARCHAR(50),
   PRIMARY KEY(name)
);

CREATE TABLE Fuel(
   type VARCHAR(50),
   PRIMARY KEY(type)
);

CREATE TABLE Cylinders(
   valeur FLOAT,
   PRIMARY KEY(valeur)
);

CREATE TABLE Gear_Box(
   type VARCHAR(50),
   PRIMARY KEY(type)
);

CREATE TABLE Engine(
   volume FLOAT,
   PRIMARY KEY(volume)
);

CREATE TABLE Airbags(
   quantity INT,
   PRIMARY KEY(quantity)
);

CREATE TABLE Drive_Wheels(
   name VARCHAR(50),
   PRIMARY KEY(name)
);

CREATE TABLE Doors(
   code VARCHAR(50),
   PRIMARY KEY(code)
);

CREATE TABLE Wheels(
   code VARCHAR(50),
   PRIMARY KEY(code)
);

CREATE TABLE Annees(
   annee INT,
   PRIMARY KEY(annee)
);
