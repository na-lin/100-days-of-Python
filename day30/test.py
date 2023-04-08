# with open("test.json",mode='x') as file:
#     pass



# dict = {
#     "GG": {
#         "email:": "angela@gmail.com",
#         "password": "0A5(*4hpRh8F(bdiT$"
#     },
#     "FSFS": {
#         "email:": "angela@gmail.com",
#         "password": "NR&b8(4k$hBA*ks3"
#     }
# }
# if "CC" in dict:
#     print("exist")

def calculate_bmi():

    height = float(input("input height: "))
    weight = int(input("input weight: "))


    if height > 2.4:
        raise ValueError("invalid height")
    # try:
    #     bmi = weight / height ** 2
    #
    # except ValueError:
    #     print("This human height is not going to exist.\nplease input vaild height.")
    #     calculate_bmi()
    # else:
    bmi = weight / height ** 2
    print(bmi)

calculate_bmi()