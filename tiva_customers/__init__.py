from argparse import ArgumentParser
import json
import os

def main():
    arguments_parser = ArgumentParser(description="Register customers.")
    arguments_parser.add_argument("command", help="customer name")
    arguments_parser.add_argument("name", help="customer name")
    arguments_parser.add_argument("--tiva-path", default="/usr/share/tiva", help="path to tiva directory")
    arguments = arguments_parser.parse_args()
    command = vars(arguments)["command"]
    name = vars(arguments)["name"]
    tiva_path = vars(arguments)["tiva_path"]
    customers_path = os.path.join(tiva_path, "customers")
    if not os.path.isdir(customers_path):
        os.mkdir(customers_path)
    if command == "add":
        customer = open(os.path.join(customers_path, "0.json"), "w")
        json.dump({
            "name": name
        }, customer)
        customer.close()
