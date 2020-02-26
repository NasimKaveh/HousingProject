import pandas as pd

def preprocess(df):

# this file removes rows containing Null value
# select columns containing string values and replace them with integers


    df=pd.read_csv('train.csv')
    df2 = df
    
#removing the null row values 
    null_data=(df2.isnull().sum()/df2.isnull().count()).sort_values(ascending=False)
    delete=null_data.head(19)
    df2=df2.drop(delete.index, axis=1)

#to select columns with string (object)
#df2_change=df2.select_dtypes(include=['object'])
 
#save file to csv to visualize
#df2_change.to_csv('df2_change.csv')

#to count number of coloums --> df2_change.count


# to get unique values of column values (objects)
# df2.column.drop_duplicates() --> shows the object contents in a column and the number of repeatition
# df2.column.unique()   --> shows only the object contents in a column e.g.: array(['RL', 'RM', 'C (all)', 'FV', 'RH'], dtype=object)

    df2.MSZoning[df2.MSZoning == 'RL'] = 0
    df2.MSZoning[df2.MSZoning == 'RM'] = 1
    df2.MSZoning[df2.MSZoning == 'C (all)'] = 2
    df2.MSZoning[df2.MSZoning == 'FV'] = 3
    df2.MSZoning[df2.MSZoning == 'RH'] = 4

# df2.column.to_csv('Street.csv')
    df2.Street[df2.Street == 'Pave'] = 1
    df2.Street[df2.Street == 'Grvl'] = 0

    df2.LotShape[df2.LotShape == 'Reg'] = 0
    df2.LotShape[df2.LotShape == 'IR1'] = 1
    df2.LotShape[df2.LotShape == 'IR2'] = 2
    df2.LotShape[df2.LotShape == 'IR3'] = 3

    df2.LandContour[df2.LandContour == 'Lvl'] = 0
    df2.LandContour[df2.LandContour == 'Bnk'] = 1
    df2.LandContour[df2.LandContour == 'Low'] = 2
    df2.LandContour[df2.LandContour == 'HLS'] = 3

    df2.Utilities[df2.Utilities == 'AllPub'] = 0
    df2.Utilities[df2.Utilities == 'NoSeWa'] = 1

    df2.LotConfig[df2.LotConfig == 'Inside'] = 0
    df2.LotConfig[df2.LotConfig == 'FR2'] = 1
    df2.LotConfig[df2.LotConfig == 'Corner'] = 2
    df2.LotConfig[df2.LotConfig == 'CulDSac'] = 3
    df2.LotConfig[df2.LotConfig == 'FR3'] = 4

    df2.LandSlope[df2.LandSlope == 'Gtl'] = 0
    df2.LandSlope[df2.LandSlope == 'Mod'] = 1
    df2.LandSlope[df2.LandSlope == 'Sev'] = 2

    df2.Neighborhood[df2.Neighborhood == 'CollgCr'] = 0
    df2.Neighborhood[df2.Neighborhood == 'Veenker'] = 1
    df2.Neighborhood[df2.Neighborhood == 'Crawfor'] = 2
    df2.Neighborhood[df2.Neighborhood == 'NoRidge'] = 3
    df2.Neighborhood[df2.Neighborhood == 'Mitchel'] = 4
    df2.Neighborhood[df2.Neighborhood == 'Somerst'] = 5
    df2.Neighborhood[df2.Neighborhood == 'NWAmes'] = 6
    df2.Neighborhood[df2.Neighborhood == 'OldTown'] = 7
    df2.Neighborhood[df2.Neighborhood == 'BrkSide'] = 8
    df2.Neighborhood[df2.Neighborhood == 'Sawyer'] = 9
    df2.Neighborhood[df2.Neighborhood == 'NridgHt'] = 10
    df2.Neighborhood[df2.Neighborhood == 'NAmes'] = 11
    df2.Neighborhood[df2.Neighborhood == 'SawyerW'] = 12
    df2.Neighborhood[df2.Neighborhood == 'IDOTRR'] = 13
    df2.Neighborhood[df2.Neighborhood == 'MeadowV'] = 14
    df2.Neighborhood[df2.Neighborhood == 'Edwards'] = 15
    df2.Neighborhood[df2.Neighborhood == 'Timber'] = 16
    df2.Neighborhood[df2.Neighborhood == 'Gilbert'] = 17
    df2.Neighborhood[df2.Neighborhood == 'StoneBr'] = 18
    df2.Neighborhood[df2.Neighborhood == 'ClearCr'] = 19
    df2.Neighborhood[df2.Neighborhood == 'NPkVill'] = 20
    df2.Neighborhood[df2.Neighborhood == 'Blmngtn'] = 21
    df2.Neighborhood[df2.Neighborhood == 'BrDale'] = 22
    df2.Neighborhood[df2.Neighborhood == 'SWISU'] = 23
    df2.Neighborhood[df2.Neighborhood == 'Blueste'] = 24

    df2.Condition1[df2.Condition1 == 'Norm'] = 0
    df2.Condition1[df2.Condition1 == 'Feedr'] = 1
    df2.Condition1[df2.Condition1 == 'PosN'] = 2
    df2.Condition1[df2.Condition1 == 'Artery'] = 3
    df2.Condition1[df2.Condition1 == 'RRAe'] = 4
    df2.Condition1[df2.Condition1 == 'RRNn'] = 5
    df2.Condition1[df2.Condition1 == 'RRAn'] = 6
    df2.Condition1[df2.Condition1 == 'PosA'] = 7
    df2.Condition1[df2.Condition1 == 'RRNe'] = 9

    df2.Condition2[df2.Condition2 == 'Norm'] = 0
    df2.Condition2[df2.Condition2 == 'Artery'] = 3
    df2.Condition2[df2.Condition2 == 'RRNn'] = 5
    df2.Condition2[df2.Condition2 == 'Feedr'] = 1
    df2.Condition2[df2.Condition2 == 'PosN'] = 2
    df2.Condition2[df2.Condition2 == 'PosA'] = 7
    df2.Condition2[df2.Condition2 == 'RRAn'] = 6
    df2.Condition2[df2.Condition2 == 'RRAe'] = 4

    df2.BldgType[df2.BldgType == '1Fam'] = 0
    df2.BldgType[df2.BldgType == '2fmCon'] = 1
    df2.BldgType[df2.BldgType == 'Duplex'] = 2
    df2.BldgType[df2.BldgType == 'TwnhsE'] = 3
    df2.BldgType[df2.BldgType == 'Twnhs'] = 4

    df2.HouseStyle[df2.HouseStyle == '2Story'] = 0
    df2.HouseStyle[df2.HouseStyle == '1Story'] = 1
    df2.HouseStyle[df2.HouseStyle == '1.5Fin'] = 2
    df2.HouseStyle[df2.HouseStyle == '1.5Unf'] = 3
    df2.HouseStyle[df2.HouseStyle == 'SFoyer'] = 4
    df2.HouseStyle[df2.HouseStyle == 'SLvl'] = 5
    df2.HouseStyle[df2.HouseStyle == '2.5Unf'] = 6
    df2.HouseStyle[df2.HouseStyle == '2.5Fin'] = 7

    df2.RoofStyle[df2.RoofStyle == 'Gable'] = 0
    df2.RoofStyle[df2.RoofStyle == 'Hip'] = 1
    df2.RoofStyle[df2.RoofStyle == 'Gambrel'] = 2
    df2.RoofStyle[df2.RoofStyle == 'Mansard'] = 3
    df2.RoofStyle[df2.RoofStyle == 'Flat'] = 4
    df2.RoofStyle[df2.RoofStyle == 'Shed'] = 5

    df2.RoofMatl[df2.RoofMatl == 'CompShg'] = 0
    df2.RoofMatl[df2.RoofMatl == 'WdShngl'] = 1
    df2.RoofMatl[df2.RoofMatl == 'Metal'] = 2
    df2.RoofMatl[df2.RoofMatl == 'WdShake'] = 3
    df2.RoofMatl[df2.RoofMatl == 'Membran'] = 4
    df2.RoofMatl[df2.RoofMatl == 'Tar&Grv'] = 5
    df2.RoofMatl[df2.RoofMatl == 'Roll'] = 6
    df2.RoofMatl[df2.RoofMatl == 'ClyTile'] = 7

    df2.Exterior1st[df2.Exterior1st == 'VinylSd'] = 0
    df2.Exterior1st[df2.Exterior1st == 'MetalSd'] = 1
    df2.Exterior1st[df2.Exterior1st == 'Wd Sdng'] = 2
    df2.Exterior1st[df2.Exterior1st == 'HdBoard'] = 3
    df2.Exterior1st[df2.Exterior1st == 'BrkFace'] = 4
    df2.Exterior1st[df2.Exterior1st == 'WdShing'] = 5
    df2.Exterior1st[df2.Exterior1st == 'CemntBd'] = 6
    df2.Exterior1st[df2.Exterior1st == 'Plywood'] = 7
    df2.Exterior1st[df2.Exterior1st == 'AsbShng'] = 8
    df2.Exterior1st[df2.Exterior1st == 'Stucco'] = 9
    df2.Exterior1st[df2.Exterior1st == 'BrkComm'] = 10
    df2.Exterior1st[df2.Exterior1st == 'AsphShn'] = 11
    df2.Exterior1st[df2.Exterior1st == 'Stone'] = 12
    df2.Exterior1st[df2.Exterior1st == 'ImStucc'] = 13
    df2.Exterior1st[df2.Exterior1st == 'CBlock'] = 14

    df2.Exterior2nd[df2.Exterior2nd == 'VinylSd'] = 0
    df2.Exterior2nd[df2.Exterior2nd == 'MetalSd'] = 1
    df2.Exterior2nd[df2.Exterior2nd == 'Wd Shng'] = 2
    df2.Exterior2nd[df2.Exterior2nd == 'HdBoard'] = 3
    df2.Exterior2nd[df2.Exterior2nd == 'Plywood'] = 7
    df2.Exterior2nd[df2.Exterior2nd == 'Wd Sdng'] = 2
    df2.Exterior2nd[df2.Exterior2nd == 'CmentBd'] = 6
    df2.Exterior2nd[df2.Exterior2nd == 'BrkFace'] = 4
    df2.Exterior2nd[df2.Exterior2nd == 'Stucco'] = 9
    df2.Exterior2nd[df2.Exterior2nd == 'AsbShng'] = 8
    df2.Exterior2nd[df2.Exterior2nd == 'Brk Cmn'] = 5
    df2.Exterior2nd[df2.Exterior2nd == 'ImStucc'] = 11
    df2.Exterior2nd[df2.Exterior2nd == 'AsphShn'] = 13
    df2.Exterior2nd[df2.Exterior2nd == 'Stone'] = 12
    df2.Exterior2nd[df2.Exterior2nd == 'Other'] = 14
    df2.Exterior2nd[df2.Exterior2nd == 'CBlock'] = 15

    df2.ExterQual[df2.ExterQual == 'Gd'] = 1
    df2.ExterQual[df2.ExterQual == 'TA'] = 2
    df2.ExterQual[df2.ExterQual == 'Ex'] = 0
    df2.ExterQual[df2.ExterQual == 'Fa'] = 3

    df2.ExterCond[df2.ExterCond == 'TA'] = 2
    df2.ExterCond[df2.ExterCond == 'Gd'] = 1
    df2.ExterCond[df2.ExterCond == 'Fa'] = 3
    df2.ExterCond[df2.ExterCond == 'Po'] = 4
    df2.ExterCond[df2.ExterCond == 'Ex'] = 0

    df2.Foundation[df2.Foundation == 'PConc'] = 0
    df2.Foundation[df2.Foundation == 'CBlock'] = 1
    df2.Foundation[df2.Foundation == 'BrkTil'] = 2
    df2.Foundation[df2.Foundation == 'Wood'] = 3
    df2.Foundation[df2.Foundation == 'Slab'] = 4
    df2.Foundation[df2.Foundation == 'Stone'] = 5

    df2.Heating[df2.Heating == 'GasA'] = 0
    df2.Heating[df2.Heating == 'GasW'] = 1
    df2.Heating[df2.Heating == 'Grav'] = 2
    df2.Heating[df2.Heating == 'Wall'] = 3
    df2.Heating[df2.Heating == 'OthW'] = 4
    df2.Heating[df2.Heating == 'Floor'] = 5


    df2.HeatingQC[df2.HeatingQC == 'Ex'] = 0
    df2.HeatingQC[df2.HeatingQC == 'Gd'] = 1
    df2.HeatingQC[df2.HeatingQC == 'TA'] = 2
    df2.HeatingQC[df2.HeatingQC == 'Fa'] = 3
    df2.HeatingQC[df2.HeatingQC == 'Po'] = 4

    df2.CentralAir[df2.CentralAir == 'Y'] = 0
    df2.CentralAir[df2.CentralAir == 'N'] = 1

    df2.KitchenQual[df2.KitchenQual == 'Gd'] = 1
    df2.KitchenQual[df2.KitchenQual == 'TA'] = 2
    df2.KitchenQual[df2.KitchenQual == 'Ex'] = 0
    df2.KitchenQual[df2.KitchenQual == 'Fa'] = 3

    df2.Functional[df2.Functional == 'Typ'] = 0
    df2.Functional[df2.Functional == 'Min1'] = 1
    df2.Functional[df2.Functional == 'Maj1'] = 2
    df2.Functional[df2.Functional == 'Min2'] = 3
    df2.Functional[df2.Functional == 'Mod'] = 4
    df2.Functional[df2.Functional == 'Maj2'] = 5
    df2.Functional[df2.Functional == 'Sev'] = 6

    df2.PavedDrive[df2.PavedDrive == 'Y'] = 0
    df2.PavedDrive[df2.PavedDrive == 'N'] = 1
    df2.PavedDrive[df2.PavedDrive == 'P'] = 2

    df2.SaleType[df2.SaleType == 'WD'] = 0
    df2.SaleType[df2.SaleType == 'New'] = 1
    df2.SaleType[df2.SaleType == 'COD'] = 2
    df2.SaleType[df2.SaleType == 'ConLD'] = 3
    df2.SaleType[df2.SaleType == 'ConLI'] = 4
    df2.SaleType[df2.SaleType == 'CWD'] = 5
    df2.SaleType[df2.SaleType == 'ConLw'] = 6
    df2.SaleType[df2.SaleType == 'Con'] = 7
    df2.SaleType[df2.SaleType == 'Oth'] = 8

    df2.SaleCondition[df2.SaleCondition == 'Normal'] = 0
    df2.SaleCondition[df2.SaleCondition == 'Abnorml'] = 1
    df2.SaleCondition[df2.SaleCondition == 'Partial'] = 2
    df2.SaleCondition[df2.SaleCondition == 'AdjLand'] = 3
    df2.SaleCondition[df2.SaleCondition == 'Alloca'] = 4
    df2.SaleCondition[df2.SaleCondition == 'Family'] = 5

    return df2