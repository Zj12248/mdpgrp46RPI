from communication.link import Link
from communication.android import AndroidLink  

def main():
    print("rpiAndroidTest Initilised")
    link = AndroidLink()
    print("AndroidLink Class Set Up")
    link.connect()
    print("Link/Connection Established")

    # Test sending a message
    message = AndroidMessage(cat="info", value="Hello from RPi!")
    link.send(message)

    # Test receiving a message
    received_message = link.recv()
    print(f"Received: {received_message}")

    link.disconnect()

if __name__ == "__main__":
    main()
