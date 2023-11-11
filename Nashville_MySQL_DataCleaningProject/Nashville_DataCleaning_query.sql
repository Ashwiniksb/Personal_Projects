-- I pushed the dataset through python by connecting the database to it using create_engine of sqlalchemy.

alter table `nashville housing data for data cleaning` rename nashville;

#####################################

select * from nashville;
select SaleDate from nashville
ORDER BY SaleDate;

#####################################

-- As you may see, SaleDate is not in date format. 
-- We update it to date format first and then perform TYPECAST
SELECT SaleDate, DATE(SaleDate) as Date_
FROM nashville;

UPDATE nashville 
SET SaleDate = DATE(SaleDate); 

ALTER TABLE nashville MODIFY SaleDate DATE;

###############################################

-- Check for null values. 
select * from nashville
WHERE PropertyAddress IS NULL;

/* Property address doesn't change and ParcelID is the code attributed to a land 
implying it is unique to each property */
-- since we can replace the nulls using the address that we fetch through parcelID, 
-- we can use IFNULL(x, y), which tells if x is null, replace with y. 

select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ifnull(a.PropertyAddress, b.PropertyAddress) as fillna
from nashville as a
JOIN nashville as b 
ON a.ParcelID = b.ParcelID 
AND a.UniqueID != b.UniqueID
Where a.PropertyAddress IS NULL;

-- Updating the nulls with the address. Remember, MySQL does not consider FROM in an UPDATE statement.
UPDATE nashville as a
JOIN nashville as b
ON a.ParcelID = b.ParcelID AND a.UniqueID <> b.UniqueID
SET a.PropertyAddress = ifnull(a.PropertyAddress, b.PropertyAddress)
WHERE a.PropertyAddress IS NULL;

###############################################

-- seperate PropertyAddress and owneraddress using delimiter and add it into two columns for Address to be better useful.
ALTER TABLE nashville ADD COLUMN Address varchar(50);
ALTER TABLE nashville ADD COLUMN State varchar(25);

-- First half goes like this
SELECT 
SUBSTRING(PropertyAddress, 1, LOCATE(',', PropertyAddress) - 1) as Address,
-- Second half goes like this
SUBSTRING(PropertyAddress, LOCATE(',', PropertyAddress) + 1, LENGTH(PropertyAddress)) as State
FROM nashville;

-- Now we update the columns.
UPDATE nashville
SET Address = SUBSTRING(PropertyAddress, 1, LOCATE(',', PropertyAddress) - 1);

UPDATE nashville
SET State = SUBSTRING(PropertyAddress, LOCATE(',', PropertyAddress) + 1, LENGTH(PropertyAddress));

-- same done to owner address but in a short-cut manner by using SUBSTRING_INDEX.
SELECT 
SUBSTRING_INDEX(OwnerAddress, ',', 1) as OwAddress,
SUBSTRING_INDEX(OwnerAddress, ',', -1) as StateAddress,
SUBSTRING_INDEX(SUBSTRING_INDEX(OwnerAddress, ',', 2), ',', -1) as CityAddress
FROM nashville;

ALTER TABLE nashville ADD COLUMN OwAddress varchar(100),
ADD COLUMN StateAddress varchar(100), 
ADD COLUMN CityAddress varchar(100);

UPDATE nashville
SET OwAddress = SUBSTRING_INDEX(OwnerAddress, ',', 1),
StateAddress = SUBSTRING_INDEX(OwnerAddress, ',', -1),
CityAddress = SUBSTRING_INDEX(SUBSTRING_INDEX(OwnerAddress, ',', 2), ',', -1);

###############################################

-- Changing Y and N from SoldAsVacant to yes and no
SELECT SoldAsVacant, COUNT(SoldAsVacant) FROM nashville 
GROUP BY SoldAsVacant;

-- we need to replace Y with Yes and N with No
UPDATE nashville
SET SoldAsVacant = 'Yes'
WHERE SoldAsVacant = 'Y';

UPDATE nashville
SET SoldAsVacant = 'No'
WHERE SoldAsVacant = 'N';

###############################################
SELECT COUNT(PropertyAddress) FROM nashville;
-- We must now check for duplicates. Unique ID as you can see, is unique. But it doesn't really show if the entries in each column are same for 2 rows. 
-- Hence we can use Windows functions to do the same. Then delete the duplicate row.

DELETE FROM nashville
WHERE UniqueID IN (
    SELECT UniqueID
    FROM (
        SELECT *,
               ROW_NUMBER() OVER (PARTITION BY ParcelID, PropertyAddress, SaleDate, SalePrice ORDER BY UniqueID) as row_num
        FROM nashville
    ) AS CTE_row_num
    WHERE row_num <> 1
);

###############################################

-- Next is the feature_selection step, where we remove unused columns (do not do this often, check with people you work with). 
-- The following is the query for the same
ALTER TABLE nashville DROP COLUMN PropertyAddress, 
DROP COLUMN OwnerAddress, 
DROP COLUMN TaxDistrict;

###############################################
-- That's it for cleaning for now. Further if we had more numerical data we would have to detect and treat outliers as well.
-- Until next time.. HAPPY LEARNING!!!




