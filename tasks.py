from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP

from RPA.Tables import csv





@task
def order_robots_from_RobotSpareBin():
     """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
     browser.configure(
        slowmo=100,
    )
     
     open_the_website()

     get_orders()

    #  close_annoying_modal()

    #  fill_the_form()

def open_the_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")

def get_orders():
    """Downloads excel file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)
 

    # table = CSV().read(output_file)


# def close_annoying_modal():
     

# def fill_the_form():
