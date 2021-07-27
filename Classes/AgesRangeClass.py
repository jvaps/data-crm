from DataFrameClass import DataFrame as dfc


class AgesRange:
    youngAdult = sum(dfc.age.values < 30)
    adults = sum((dfc.age.values > 30) & (dfc.age.values < 50))
    seniorAdult = sum((dfc.age.values > 50) & (dfc.age.values < 70)),
    senior = sum(dfc.age.values > 70)
