MEMBER_1 = "Drew"
MEMBER_2 = "Ayaz"
MEMBER_3 = "Brian"

MEMBER_1_HOME = "Ann Arbor, MI"
MEMBER_2_HOME = "Baku, Azerbaijan"
MEMBER_3_HOME = "Farmington Hills, Michigan"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")