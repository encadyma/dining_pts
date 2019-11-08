# Direct URLS
URL_AUTH_PORTAL = "https://cal.berkeley.edu/login/"

# Current data on Cal Dining
META_SCHOOL_YR = "2019-20"

# I suppose these are the enums.
BREAKFAST = 0x10
BRUNCH = 0x1b
LUNCH = 0x20
LUNCH_CONT = 0x2d
DINNER = 0x30
LATE_NIGHT = 0x70

LOC_CROADS = 0xd10
LOC_CAFE3 = 0xd20
LOC_FOOTHILL = 0xd30
LOC_CLARK = 0xd40

LOC_BROWNS = 0xc10
LOC_GBC = 0xc20

# On-campus Dining Limits (per week or sem)
LIMIT_SWIPES_BP = 12
LIMIT_SWIPES_GP = 10
LIMIT_SWIPES_UL = None

LIMIT_FLEXD_BP = 300
LIMIT_FLEXD_GP = 500
LIMIT_FLEXD_UL = 500

# Off-campus Dining Limits
LIMIT_FLEXD_1400 = 700
LIMIT_FLEXD_1900 = 950
LIMIT_FLEXD_2700 = 1350

LIMIT_SWIPES_OFFCAMPUS = 0

# Pricing in Dining Commons
# (lunch = brunch)
COST_BREAKFAST_SELF = 7
COST_BREAKFAST_GUEST = 7
COST_BREAKFAST_NONE = 10

COST_LUNCH_SELF = 8
COST_LUNCH_GUEST = 8
COST_LUNCH_NONE = 13

COST_DINNER_SELF = 9
COST_DINNER_GUEST = 9
COST_DINNER_NONE = 14

# Regular Start/End Times ~ exclusive
# (this should typically overriden by
#  the website schedules, which provide
#  location specific times.)

TIMETABLES_WEEKDAY = [
    (BREAKFAST, "07:00", "9:30"),
    (LUNCH, "11:00", "14:00"),
    (LUNCH_CONT, "14:00", "17:00"),
    (DINNER, "17:00", "20:30"),
    (LATE_NIGHT, "22:00", "25:30")
]

TIMETABLES_WEEKEND = [
    (BRUNCH, "10:00", "14:30"),
    (DINNER, "17:00", "20:30")
]
