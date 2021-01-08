#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program formats your address appropriately

def formatter(address, street_number, street_name, city,
             province, postal_code, apt_number = None):
    # This function formats your address appropriately

    if apt_number is not None:
        formated_address = (address + "\n" + apt_number + "-" +
                            street_number + " " + street_name + "\n" +
                            city + " " + province + " " + postal_code)
    else:
        formated_address = (address + "\n" + street_number + " " +
                            street_name + "\n" + city + " " + province +
                            " " + postal_code)

    return formated_address


def main():
    # This function collects inputs and gives them to the formater

    print("Please enter your address information\n")

    address_input = input("Address: ")
    apartment_check = input("Do you live in a unit, suite"
                            " or apartment (Y/N)?: ")

    if apartment_check == "Y" or apartment_check == "YES":
        apt_number_input = input("Apt. number: ")
    else:
        apt_number_input = None

    street_number_input = input("Street number: ")
    street_name_input = input("Street name: ")
    city_input = input("City: ")
    province_input = input("Province (abbreviated): ")
    postal_code_input = input("Postal code: ")
    print("")

    final_product = formatter(address_input, street_number_input,
                             street_name_input, city_input, province_input,
                             postal_code_input, apt_number_input)

    print(final_product)


if __name__ == "__main__":
    main()
