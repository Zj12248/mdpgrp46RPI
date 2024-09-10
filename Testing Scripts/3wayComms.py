from communication.link import Link
from communication.stm32 import STMLink
from communication.android import AndroidLink  # Ensure this import is correct
import json

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
            r_message: dict = json.loads(received_message)
            # If received message is a command
            if message['cat'] == 'info':
                movement_command = r_message['value']
                print(f"Movement Command: {movement_command}")


            # Send using message received from android
            print(f"Sending command to STM32: {movement_command}")
            stm_link.send(movement_command)

            ''' 
            # send direct from rpi  
            test_command = "FW01"     
            print(f"Sending command to STM32: {test_command}")
            stm_link.send(test_command) 
            '''
            
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
