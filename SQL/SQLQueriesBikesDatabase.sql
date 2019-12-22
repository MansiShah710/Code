-- Create a Bikes database and load data into it

create database Bikes;
use Bikes;


-- Product table
create table Product
(ProductID integer not null,
ProductName varchar(50),
Cost real,
WholeSalePrice real,
MSRP real,
constraint Product_PK primary key (ProductID)
);

-- Customer table
create table Customer
(CustomerID integer not null,
CustomerFirstName varchar(50),
CustomerLastName varchar(50),
CustomerAddress varchar(50),
CustomerAge integer,
CustomerExperience integer,
constraint Customer_PK primary key (CustomerID)
);

-- Department table
create table Department
(DepartmentID integer not null,
DepartmentName varchar(50),
constraint Department_PK primary key (DepartmentID)
);

-- Region table
create table Region
(RegionID integer not null,
RegionName varchar(50),
constraint Region_PK primary key (RegionID)
);

-- Employee table
create table Employee
(EmployeeID integer not null,
EmployeeFirstName varchar(50),
EmployeeLastName varchar(50),
DepartmentID integer,
EmployeeAddress varchar(50),
Gender varchar(1),
EmployeeBirthDate date,
Salary real,
RegionID integer,
constraint Employee_PK primary key (EmployeeID),
constraint Employee_FK1 foreign key (DepartmentID) references Department(DepartmentID),
constraint Employee_FK2 foreign key (RegionID) references Region(RegionID)
);

-- SalesOrder table
create table SalesOrder
(OrderID integer not null,
PODate date,
ProductID integer,
CustomerID integer,
CustomerPO integer,
EmployeeID integer,
Quantity integer,
UnitPrice real,
constraint SalesOrder_PK primary key (OrderID),
constraint SalesOrder_FK1 foreign key (CustomerID) references Customer(CustomerID),
constraint SalesOrder_FK2 foreign key (ProductID) references Product(ProductID),
constraint SalesOrder_FK3 foreign key (EmployeeID) references Employee(EmployeeID)
);

-- Bulk insert the data into the table
BULK
INSERT Product
FROM 'C:\Users\student\Downloads\Product.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT Customer
FROM 'C:\Users\student\Downloads\Customer.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT Department
FROM 'C:\Users\student\Downloads\Department.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT Region
FROM 'C:\Users\student\Downloads\Region.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT Employee
FROM 'C:\Users\student\Downloads\Employee.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT SalesOrder
FROM 'C:\Users\student\Downloads\SalesOrder.txt'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO



-- Query 1: Display the total sales in each region for products Extreme Mountain Bike, Extreme Plus Mountain Bike, and Extreme Ultra Mountain Bike.Total Sales is quantity times unit price for each transaction.

select r.RegionName,
 	   sum(s.Quantity * s.UnitPrice) as [Total Sales]
from Employee emp
inner join Region r on emp.RegionID = r.RegionID
inner join SalesOrder s on emp.EmployeeID = s.EmployeeID
where s.ProductID in (select ProductID from Product where ProductName in ('Extreme Mountain Bike', 'Extreme Plus Mountain Bike', 'Extreme Ultra Mountain Bike'))
group by r.RegionName
order by r.RegionName;


-- Query 2: Display the ProductID, ProductName,and Cost of the products which are NOT purchased by the customer Dan Connor.

select ProductID,
   	   ProductName,
       Cost
from Product
where ProductID not in
(select ProductId from SalesOrder where CustomerID in (select CustomerID from Customer where CustomerFirstName = 'Dan' and CustomerLastName = 'Connor'));

--Query 3: Display the CustomerID, CustomerFirstName, CustomerLastName, CustomerAge of the customers whose age is above average and has created more than 1000 OrderIDs.Your query should also display the average age as �AvgAge� of the customers.

select cust.CustomerID,
	   CustomerFirstName,
	   CustomerLastName,
	   CustomerAge,
	   AverageAge
from Customer cust
inner join (select CustomerID from SalesOrder group by CustomerID having count(OrderID) > 1000) s on cust.CustomerID = s.CustomerID
inner join (select avg(CustomerAge) from Customer) derived_t(AverageAge) on cust.CustomerAge > AverageAge;

--Query4. Display the maximum sales by a customer in each quarter.

select max(Q1) as [Max Sales Q1],
	   max(Q2) as [Max Sales Q2],
   	   max(Q3) as [Max Sales Q3],
       max(Q4) as [Max Sales Q4]
FROM (select * FROM
	 ( select s.CustomerID, s.Qtr, sum(s.Quantity * s.UnitPrice) as [Total Sales] from (
	 select CustomerID,
	 CASE
	 WHEN PODate >= '2014-01-01' AND PODate < '2014-04-01' THEN 'Q1'
	 WHEN PODate >= '2014-04-01' AND PODate < '2014-07-01' THEN 'Q2'
	 WHEN PODate >= '2014-07-01' AND PODate < '2014-10-01' THEN 'Q3'
	 WHEN PODate >= '2014-10-01' AND PODate <= '2014-12-31' THEN 'Q4'
	 END AS Qtr,
	 Quantity, UnitPrice from SalesOrder) s
 group by s.CustomerID, s.Qtr) t
 PIVOT(sum([Total Sales]) FOR [Qtr] IN (Q1, Q2, Q3, Q4)) as Pivottable) p;


-- Query 5: Display the ProductName and �Over Avg Profit� for the products whose total profit from all the transactions is above the average profit. The profit is given by Quantity * (UnitPrice � Cost). 

Go
CREATE VIEW [PAverage] As
select p.ProductID,
	   p.ProductName,
       sum(s.Quantity * (s.UnitPrice - p.Cost)) as Profit
from SalesOrder s
inner join Product p on s.ProductID = p.ProductID
group by p.ProductID, p.ProductName;
GO

select PAverage.ProductName,
	   PAverage.Profit as OverAvgProfit
from PAverage, (select Avg(Profit) from PAverage) derived_t(AvgP)
where PAverage.Profit > derived_t.AvgP
group by PAverage.ProductName, PAverage.Profit
order by OverAvgProfit;


