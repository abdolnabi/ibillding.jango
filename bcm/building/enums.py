class ResidenceType:
    BUILDING = 'BUILDING'
    TOWN = 'TOWN'
    COMPLEX = 'COMPLEX'
    LOCAL_SHOP = 'LOCAL_SHOP'


class FacilityType:
    RESIDENCE = 'RESIDENCE'
    BLOCK = 'BLOCK'
    UNIT = 'UNIT'
    ALL = 'ALL'


class UnitUserType:
    RESIDENT = 'RESIDENT'
    OWNER = 'OWNER'
    BOTH = 'BOTH'


class FacilityResidenceAccessibilitiesType:
    PUBLIC = 'PUBLIC'
    UNIT = 'UNIT'
    RESIDENCE = 'RESIDENCE'
    BLOCK = 'BLOCK'


class BillClassType:
    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'


class BillType:
    SETTLEMENT_REQUEST = 'SETTLEMENT_REQUEST'
    ADVERTISEMENT = 'ADVERTISEMENT'
    REQUEST = 'REQUEST'
    BUDGET = 'BUDGET'


class BillCurrency:
    IRR = 'IRR'
    USD = 'USD'


class BillStatus:
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    REJECTED = 'REJECTED'
    EXPIRED = 'EXPIRED'


class AdvertisementType:
    LOCAL = 'LOCAL'
    GLOBAL = 'GLOBAL'


class AdvertisementStatus:
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'


class PaymentStatus:
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    REJECTED = 'REJECTED'
    EXPIRED = 'EXPIRED'


class BudgetClassType:
    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'
