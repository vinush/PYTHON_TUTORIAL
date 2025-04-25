# def welcome():
#     print("Welcome to my program")


# def func1():
#     print("func1 is being called")


# def main():
#     welcome()
#     func1()


# if __name__ == "__main__":
#     print("sub_module is being run directly")
#     main()
# else:
#     print("sub_module is being imported into another module")

from codexplore import emailProcess, printMsg


def main():
    emails = ["thangnt@hocmai.vn", "tungtt@gmail.com", "duynh@gmail.com"]
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printMsg(email_username, email_domain)


if __name__ == "__main__":
    main()
