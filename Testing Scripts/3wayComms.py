from communication.link import Link
from communication.stm32 import STMLink
from communication.android import AndroidLink  # Ensure this import is correct

def main():
    print("rpiAndroidTest Initialized")
    link = AndroidLink()
    
    try:
        # Set up AndroidLink and connect
        print("AndroidLink Class Set Up")
        link.connect()
        print("Link/Connection Established")
        
        stm_link = STMLink()
        
        # Connect to STM32
        try:
            stm_link.connect()
            print("Connected to STM32 successfully.")
            
            # Test sending a message to Android
            message = AndroidMessage(cat="info", value="Hello from RPi!")
            link.send(message)
            
            # Test receiving a message from Android
            received_message = link.recv()
            print(f"Received: {received_message}")

            # Test sending a command to STM32
            test_command = "FW01"  # Move forward 1 unit as an example command
            print(f"Sending command to STM32: {test_command}")
            stm_link.send(test_command)
            
            # Wait for acknowledgment from STM32
            ack = stm_link.recv()
            if ack == "ACK":
                print("STM32 acknowledged the command.")
                ackMessage = AndroidMessage(cat="info", value="STM32 ACK")
                link.send(ackMessage)
            else:
                print(f"Unexpected response from STM32: {ack}")
        
        except Exception as e:
            print(f"Error connecting to STM32 or sending command: {e}")

        finally:
            # Disconnect from STM32
            stm_link.disconnect()
            print("Disconnected from STM32.")
    
    except Exception as e:
        print(f"Error connecting to Android or sending message: {e}")
    
    finally:
        # Disconnect from Android
        link.disconnect()
        print("Disconnected from Android.")

if __name__ == "__main__":
    main()
