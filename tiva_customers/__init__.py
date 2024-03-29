from argparse import ArgumentParser
import json
import os

def main():
    arguments_parser = ArgumentParser(description="Register customers.")
    arguments_parser.add_argument("command", help="customer name")
    arguments_parser.add_argument("args", nargs="*", help="command arguments")
    arguments_parser.add_argument("--tiva-path", default="/usr/share/tiva", help="path to tiva directory")
    arguments = arguments_parser.parse_args()
    command = vars(arguments)["command"]
    args = vars(arguments)["args"]
    tiva_path = vars(arguments)["tiva_path"]
    customers_path = os.path.join(tiva_path, "customers")
    if not os.path.isdir(customers_path):
        os.mkdir(customers_path)
    if command == "add":
        name = args[0]
        customer_id = max(map(lambda filename: int(filename.split(".")[0]), os.listdir(customers_path)) + [-1]) + 1
        customer = open(os.path.join(customers_path, "%s.json" % customer_id), "w")
        json.dump({
            "name": name
        }, customer)
        customer.close()
    if command == "getid":
        name = args[0]
        for filename in os.listdir(customers_path):
            customer = json.load(open(os.path.join(customers_path, filename)))
            if customer["name"] == name:
                customer_id = filename.split(".")[0]
                print customer_id
                return
    if command == "rm":
        customer_id = args[0]
        customer_path = os.path.join(customers_path, "%s.json" % customer_id)
        os.remove(customer_path)
    if command == "get":
        customer_id = args[0]
        key = args[1]
        customer_path = os.path.join(customers_path, "%s.json" % customer_id)
        customer = json.load(open(customer_path))
        print customer[key]
    if command == "set":
        customer_id = args[0]
        key = args[1]
        value = args[2]
        customer_path = os.path.join(customers_path, "%s.json" % customer_id)
        customer = json.load(open(customer_path))
        customer[key] = value
        json.dump(customer, open(customer_path, "w"))
